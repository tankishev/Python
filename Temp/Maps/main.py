from csv import reader
from DataObjects.utilities import print_execution_time, save_object, calc_distance
from Temp.Maps.DataObjects import Credit, Observation, CreditObservations, ResidentialAddress, PermanentAddress
from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def get_data_from_excel():
    observations = []
    filename = ''
    with open(filename, 'r') as read_obj:
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

    save_object(observations, 'Data/credit.observations')


def radius_search_by_id(search_for='100331054', radius=300, verbose=False):

    # set-up
    file_name = 'Data/credit.observations'
    observations = CreditObservations(file_name)
    observations.load_data()

    # check for searched item
    if all(item.credit.creditid != search_for for item in observations):
        if verbose:
            return print(f"No observation with CreditID {search_for}")
        return None
    record_a = next(item for item in observations if item.credit.creditid == search_for)

    # filter incomplete observations
    filtered_observations = observations.filter(g_status='OK', country='Bulgaria')
    filtered_observations = filtered_observations.filter(creditid=search_for, exclude=True)

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
    if verbose:
        print(f'{len(output)} loans at distance {radius}km from {("Good", "Bad")[record_a.credit.bad_flag]} '
              f'CreditID {search_for}')
        share_bad = len([el for el in output if el[1] == 'Bad']) / len(output)
        print(f'Share of bad loans: {share_bad:.2f}')
        print(*output, sep='\n')
    else:
        retval = {el[0] for el in output}
        retval.add(search_for)
        return retval


@print_execution_time
def get_clusters_by_radius(radius=10, min_cluster_size=10):

    # set-up
    file_name = 'Data/credit.observations'

    # read observations
    observations = CreditObservations(file_name)
    observations.load_data()
    filtered_observations = observations.filter(g_status='OK', country='Bulgaria')

    # get distances for each point
    performance = {}
    v_distance = np.vectorize(calc_distance)
    for record_a in filtered_observations:
        other_records = [el for el in filtered_observations if el != record_a]

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
    file_name = 'Data/credit.observations'

    # read observations
    observations = CreditObservations(file_name)
    observations.load_data()

    try:
        found_record = next(item for item in observations.filter(creditid=search_for))
        print(found_record.get_info())
    except StopIteration:
        print('No record found')


def update_records():

    # read observations
    file_name = 'Data/credit.observations'
    observations = CreditObservations(file_name)
    observations.load_data()

    # update Prepaid and Paid not as bad
    i = 0
    for record in observations:
        if record.credit.status in ('Предсрочно погасен', 'Погасен') and record.credit.bad_flag:
            record.credit.bad_flag = False
            i += 1

    print(f'{i} records updated')
    save_object(observations, file_name)


def update_dpd(max_dpd_active=60, max_dpd_repaid=90, repaid_statuses=('Предсрочно погасен', 'Погасен')):
    filename = ''
    with open(filename, 'r') as read_obj:
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

    file_name = 'Data/credit.observations'
    observations = CreditObservations(file_name)
    observations.load_data()

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



def plot_points():

    # read observations
    file_name = 'Data/credit.observations'
    observations = CreditObservations(file_name)
    observations.load_data()

    # filter observations
    filtered_observations = observations.filter(g_status='OK', country='Bulgaria')

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


def plot_using_dbscan(distance_in_km: int, min_points: int, print_bad_rate=False):

    # set-up
    kms_per_radian = 6371.0088
    epsilon = distance_in_km / kms_per_radian
    num_points = min_points
    img = plt.imread("bulgaria.png")

    # read observations
    file_name = 'Data/credit.observations'
    observations = CreditObservations(file_name)
    observations.load_data()

    # filter observations
    filtered_observations = observations.filter(g_status='OK', country='Bulgaria', is_bad=True)

    # prepare data
    coord = np.array(filtered_observations.coordinates_reversed)
    x = np.radians(coord)

    # run algorithm
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
    index_by_cluster = {}
    for i, cluster_id in enumerate(cluster_labels):
        if cluster_id != -1:
            if cluster_id not in index_by_cluster.keys():
                index_by_cluster[cluster_id] = []
            index_by_cluster[cluster_id].append(filtered_observations[i].credit.creditid)

    filter_array = [el != -1 for el in cluster_labels]
    x_2 = x[filter_array]
    cluster_labels_2 = cluster_labels[filter_array]
    filtered_observations_2 = [item for i, item in enumerate(filtered_observations) if filter_array[i]]
    output = [(item.credit.creditid, item.google_address.formatted_address, item.google_address.coordinates)
              for item in filtered_observations_2]
    output = sorted(output, key=lambda item: item[2]['lng'])
    # print(len(filtered_observations_2))
    # print(*output, sep='\n')

    # get the good ones close to the cores
    core_observations = [item.credit.creditid for i, item in enumerate(filtered_observations)
                         if i in db.core_sample_indices_]

    # print(set(cluster_labels))
    if print_bad_rate:
        for key, value in index_by_cluster.items():
            bad_rates(value)
    else:
        print(*index_by_cluster.items(), sep='\n')

    fig, ax = plt.subplots()
    ax.scatter(x_2[:, 0], x_2[:, 1], c=cluster_labels_2, cmap="viridis")
    x_left, x_right = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    # ax.axes.set_aspect(abs((x_right-x_left)/(y_low-y_high))/1)
    # offset = -0.001
    # ax.imshow(img, extent=[x_left+offset, x_right+offset, y_low+offset, y_high+offset])

    plt.show()


def bad_rates(cluster_points):
    output = []
    for el in cluster_points:
        result = radius_search_by_id(el, 1)
        for item in result:
            output.append(item)
    print([item for item in set(output)])
    bad_rate = len(cluster_points) * 100 / len(set(output))
    print(f'Bad rate: {bad_rate:.2f}')


if __name__ == '__main__':

    # update_records()
    # update_dpd()
    # download_maps_data(200)
    # radius_search_by_id('100293378', 10, verbose=True)
    # view_record('100313259')
    # get_clusters_by_radius(1, 5)
    plot_points()
    # plot_using_dbscan(1, 5, print_bad_rate=False)
    # pass

