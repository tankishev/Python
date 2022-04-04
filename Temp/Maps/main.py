import matplotlib.pyplot
from Temp.Maps import save_object, read_object_from_file, calc_distance, GeocodingAPI, print_execution_time
from csv import reader
from credit_observation import Credit, Observation
from locations import ResidentialAddress, PermanentAddress
from ratelimit import RateLimiter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import DBSCAN


def get_data_from_excel():
    observations = []

    with open('A1_Info_2.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        i = 0
        for row in csv_reader:
            if i > 0:
                credit = Credit(row[0], row[3], (row[10] == '0'))

                if row[14] != 'NULL':
                    address = ResidentialAddress(row[14])
                elif row[13] != 'NULL':
                    address = PermanentAddress(row[13])
                elif row[7] != 'NULL':
                    address = ResidentialAddress(row[7], True)
                elif row[8] != 'NULL':
                    address = PermanentAddress(row[8], True)
                else:
                    address = None

                if credit and address:
                    observations.append(Observation(credit, address))
            i += 1

    save_object(observations, 'credit.observations')


@print_execution_time
def radius_search_by_id(search_for='100331054', radius=300):

    def filter_func(item):
        return item.google_address is not None \
            and item.google_address.geocoding_data.get('status', None) == 'OK' \
            and item.credit.creditid != search_for \
            and item.google_address.address_components['country'] == 'Bulgaria'

    # set-up
    file_name = 'credit.observations'

    # read observations
    observations = read_object_from_file(file_name)

    # check for searched item
    if all(item.credit.creditid != search_for for item in observations):
        return print(f"No observation with CreditID {search_for}")
    record_a = next(item for item in observations if item.credit.creditid == search_for)

    # filter incomplete observations
    filtered_observations = list(filter(filter_func, observations))

    # calculate distance to point
    lat_a = record_a.google_address.coordinates.get('lat')
    lng_a = record_a.google_address.coordinates.get('lng')
    ar_lat_b = np.array([record.google_address.coordinates.get('lat') for record in filtered_observations])
    ar_lng_b = np.array([record.google_address.coordinates.get('lng') for record in filtered_observations])

    v_distance = np.vectorize(calc_distance)
    np_distance = v_distance(lat_a, lng_a, ar_lat_b, ar_lng_b)

    output = [(item.credit.creditid,
               ("Good", "Bad")[item.credit.bad_flag],
               np_distance[i],
               item.google_address.formatted_address)
              for i, item in enumerate(filtered_observations)]

    output = list(filter(lambda x: x[2] <= radius, output))
    output = sorted(output, key=lambda x: x[2])
    print(f'{len(output)} loans at distance {radius}km from {("Good", "Bad")[record_a.credit.bad_flag]} '
          f'CreditID {search_for}')
    share_bad = len([el for el in output if el[1] == 'Bad']) / len(output)
    print(f'Share of bad loans: {share_bad:.2f}')
    print(*output, sep='\n')


@print_execution_time
def get_clusters_by_radius(radius=10, min_cluster_size=10):

    def filter_func(item):
        criteria = [
            item.google_address.geocoding_data.get('status', None) == 'OK',
            item.google_address is not None,
            item.google_address.address_components['country'] == 'Bulgaria'
        ]
        return all(criteria)

    # set-up
    file_name = 'credit.observations'

    # read observations
    observations = read_object_from_file(file_name)
    filtered_observations = list(filter(filter_func, observations))

    # get distances for each point
    performance = {}
    v_distance = np.vectorize(calc_distance)
    for record_a in filtered_observations:
        other_records = list(filter(lambda x: x != record_a, filtered_observations))

        lat_a = record_a.google_address.coordinates.get('lat')
        lng_a = record_a.google_address.coordinates.get('lng')
        ar_lat_b = np.array([record.google_address.coordinates.get('lat') for record in other_records])
        ar_lng_b = np.array([record.google_address.coordinates.get('lng') for record in other_records])

        np_distance = v_distance(lat_a, lng_a, ar_lat_b, ar_lng_b)

        output = [item for i, item in enumerate(other_records) if np_distance[i] <= radius]
        count = len(output) + 1
        if count >= min_cluster_size:
            count_bad = len([item for item in output if item.credit.bad_flag])
            if record_a.credit.bad_flag:
                count_bad += 1
            performance[record_a.credit.creditid] = (count_bad/count, count, record_a.credit.bad_flag)

    sorted_dict = sorted(performance.items(), key=lambda item: -item[1][0])
    print(*sorted_dict, sep='\n')


def view_record(search_for='100331054'):
    # set-up
    file_name = 'credit.observations'

    # read observations
    observations = read_object_from_file(file_name)

    try:
        found_record = next(item for item in observations if item.credit.creditid == search_for)
        print(found_record.get_info())
    except StopIteration:
        print('No record found')


def update_records():

    # read observations
    file_name = 'credit.observations'
    observations = read_object_from_file(file_name)

    # update Prepaid and Paid not as bad
    i = 0
    for record in observations:
        if record.credit.status in ('Предсрочно погасен', 'Погасен') and record.credit.bad_flag:
            record.credit.bad_flag = False
            i += 1

    print(f'{i} records updated')
    save_object(observations, file_name)


def update_dpd(max_dpd_active=60, max_dpd_repaid=90, repaid_statuses=('Предсрочно погасен', 'Погасен')):
    with open('A1_Info_2.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        dpd_data = {}
        i = 0
        for row in csv_reader:
            if i == 0:
                continue
            if (row[3] in repaid_statuses and int(row[6]) >= max_dpd_repaid) or \
                    (row[3] not in repaid_statuses and int(row[6]) >= max_dpd_active):
                dpd_data[row[0]] = True
            else:
                dpd_data[row[0]] = False
            i += 1

    file_name = 'credit.observations'
    observations = read_object_from_file(file_name)

    i = 0
    for record in observations:
        if record.credit.creditid in dpd_data.keys():
            flag = dpd_data.get(record.credit.creditid)
            if flag != record.credit.bad_flag:
                i += 1
                record.credit.bad_flag = flag

    if i > 0:
        save_object(observations, file_name)
        print(f'{i} observations updated')


@print_execution_time
def download_maps_data(max_records_to_download: int):

    @RateLimiter(10, 1)
    def rate_limited_google_call(conn, address):
        conn.get_location_data(address, region='BG')
        retval = conn.get_address()
        return retval

    # config
    file_name = 'credit.observations'
    extract_size = max_records_to_download

    # read observations
    observations = read_object_from_file(file_name)

    # filter incomplete observations
    records = list(filter(lambda item: item.google_address is None and not item.address.incomplete, observations))

    # extract data
    i = 0
    connector = GeocodingAPI('json')
    for record in records:
        g_address = rate_limited_google_call(connector, record.address.address)
        record.google_address = g_address
        i += 1
        if i >= extract_size:
            break
    print(f'Addresses downloaded: {i}\nItems left: {len(records) - i}')

    # save data
    save_object(observations, file_name)


def plot_points():

    def filter_func(item):
        return item.google_address is not None \
              and item.google_address.geocoding_data.get('status', None) == 'OK' \
              and item.google_address.address_components['country'] == 'Bulgaria'

    # read observations
    file_name = 'credit.observations'
    observations = read_object_from_file(file_name)

    # filter observations
    filtered_observations = list(filter(filter_func, observations))

    # prepare data
    data = {
        'lat': [item.google_address.coordinates['lat'] for item in filtered_observations],
        'lng': [item.google_address.coordinates['lng'] for item in filtered_observations],
        'is_bad': [('good', 'bad')[item.credit.bad_flag] for item in filtered_observations]
    }

    df = pd.DataFrame(data)

    # plot data
    groups = df.groupby('is_bad')
    img = plt.imread("bulgaria.png")

    fig, ax = plt.subplots()

    ax.imshow(img, extent=[22.10921, 28.88864, 41.10054, 44.3931])
    for name, group in groups:
        ax.plot(group.lng, group.lat, marker='o', linestyle='', markersize=12, label=name)

    x_left, x_right = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    ax.axes.set_aspect(abs((x_right-x_left)/(y_low-y_high))/1.6)

    plt.legend()
    plt.show()


def plot_using_dbscan():
    def filter_func(item):
        return item.google_address is not None \
            and item.google_address.geocoding_data.get('status', None) == 'OK' \
            and item.google_address.address_components['country'] == 'Bulgaria' \
            and item.credit.bad_flag

    # set-up
    kms_per_radian = 6371.0088
    epsilon = 1 / kms_per_radian
    num_points = 5
    img = plt.imread("bulgaria.png")

    # read observations
    file_name = 'credit.observations'
    observations = read_object_from_file(file_name)

    # filter observations
    filtered_observations = list(filter(filter_func, observations))

    # prepare data
    data = {
        'lat': [item.google_address.coordinates['lat'] for item in filtered_observations],
        'lng': [item.google_address.coordinates['lng'] for item in filtered_observations],
        'is_bad': [('good', 'bad')[item.credit.bad_flag] for item in filtered_observations]
    }
    df = pd.DataFrame(data)
    df_coords = df[['lng', 'lat']]
    coord = df_coords.to_numpy()
    x = np.radians(coord)
    db = DBSCAN(eps=epsilon, min_samples=num_points, algorithm='ball_tree', metric='haversine').fit(x)
    cluster_labels = db.labels_
    n_clusters = len(set(cluster_labels))
    n_noise = list(cluster_labels).count(-1)
    clusters = pd.Series([coord[cluster_labels == n] for n in range(n_clusters)])
    print(f'Data points: {len(filtered_observations)}')
    print(f'Cluster labels: {len(cluster_labels)}')
    print(f'Number of clusters: {n_clusters}')
    print(f'Number of noise points: {n_noise}')

    # some after work
    filter_array = [el != -1 for el in cluster_labels]
    x_2 = x[filter_array]
    cluster_labels_2 = cluster_labels[filter_array]
    filtered_observations_2 = [item for i, item in enumerate(filtered_observations) if filter_array[i]]
    output = [(item.credit.creditid, item.google_address.formatted_address, item.google_address.coordinates)
              for item in filtered_observations_2]
    output = sorted(output, key=lambda item: item[2]['lng'])
    print(len(filtered_observations_2))
    print(*output, sep='\n')

    # get the good ones close to the cores
    core_observations = [item.credit.creditid for i, item in enumerate(filtered_observations)
                         if i in db.core_sample_indices_]

    print(set(cluster_labels))

    fig, ax = plt.subplots()
    ax.scatter(x_2[:, 0], x_2[:, 1], c=cluster_labels_2, cmap="viridis")
    x_left, x_right = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    # ax.axes.set_aspect(abs((x_right-x_left)/(y_low-y_high))/1)
    # ax.imshow(img, extent=[x_left, x_right, y_low, y_high])

    plt.show()


if __name__ == '__main__':

    # update_records()
    # update_dpd()
    download_maps_data(200)
    # radius_search_by_id('100313259', 1)
    # view_record('100313259')
    # view_record('100309734')
    # get_clusters_by_radius(2, 5)
    # plot_points()
    # plot_using_dbscan()
    # pass
