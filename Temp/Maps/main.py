from Temp.Maps import save_object, read_object_from_file, calc_distance, GeocodingAPI, print_execution_time
from csv import reader
from credit_observation import Credit, Observation
from locations import ResidentialAddress, PermanentAddress
from ratelimit import RateLimiter
import numpy as np


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

    # set-up
    file_name = 'credit.observations'

    # read observations
    observations = read_object_from_file(file_name)

    # check for searched item
    if all(item.credit.creditid != search_for for item in observations):
        return print(f"No observation with CreditID {search_for}")
    record_a = next(item for item in observations if item.credit.creditid == search_for)

    # filter incomplete observations
    filter_func = lambda item: item.google_address is not None \
                               and item.google_address.geocoding_data.get('status', None) == 'OK' \
                               and item.credit.creditid != search_for \
                               and item.google_address.address_components['country'] == 'Bulgaria'
    filtered_observations = list(filter(filter_func, observations))

    # calculate distance to point
    lat_a = record_a.google_address.coordinates.get('lat')
    lng_a = record_a.google_address.coordinates.get('lng')
    ar_lat_b = np.array([record.google_address.coordinates.get('lat') for record in filtered_observations])
    ar_lng_b = np.array([record.google_address.coordinates.get('lng') for record in filtered_observations])

    v_distance = np.vectorize(calc_distance)
    np_distance = v_distance(lat_a, lng_a, ar_lat_b, ar_lng_b)

    output = [(item.credit.creditid, ("Good", "Bad")[item.credit.bad_flag], np_distance[i], item.google_address.formatted_address)
              for i, item in enumerate(filtered_observations)]

    output = list(filter(lambda x: x[2] <= radius, output))
    output = sorted(output, key=lambda x: x[2])
    print(f'{len(output)} loans at distance {radius}km from {("Good", "Bad")[record_a.credit.bad_flag]} '
          f'CreditID {search_for}')
    print(*output, sep='\n')


@print_execution_time
def get_clusters_by_radius(radius=10, min_cluster_size=10):

    # set-up
    file_name = 'credit.observations'
    filter_func = lambda item: item.google_address is not None \
                               and item.google_address.geocoding_data.get('status', None) == 'OK' \
                               and item.google_address.address_components['country'] == 'Bulgaria'

    # read observations
    observations = read_object_from_file(file_name)
    filtered_observations = list(filter(filter_func, observations))

    # get distances for each point
    clusters = set()
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

        # output.append(record_a.credit.creditid)
        # clusters.add(tuple(sorted(output)))

    # print(f'{len(clusters)} clusters identified')
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
def download_maps_data():

    @RateLimiter(10, 1)
    def rate_limited_google_call(conn, address):
        conn.get_location_data(address, region='BG')
        retval = conn.get_address()
        return retval

    # config
    file_name = 'credit.observations'
    extract_size = 200

    # read observations
    observations = read_object_from_file(file_name)

    # filter incomplete observations
    filter_observations = lambda item: item.google_address is None and not item.address.incomplete
    records = list(filter(filter_observations, observations))

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


if __name__ == '__main__':

    # update_records()
    update_dpd()
    # download_maps_data()
    # radius_search_by_id('100295773', 2)
    # view_record('100295773')
    # view_record('100309734')
    # get_clusters_by_radius(2, 5)
    # pass

