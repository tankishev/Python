from DataObjects.utilities import save_object, load_object, print_execution_time
from Temp.Maps.utilities.ratelimit import RateLimiter
from GoogleData import GeocodingAPI


@print_execution_time
def download_maps_data(address_dict: dict, extract_size=200):

    @RateLimiter(10, 1)
    def rate_limited_google_call(conn, address):
        retval = conn.get_location_data(address, region='BG')
        # retval = conn.get_address()
        return retval

    # set_up
    connector = GeocodingAPI('json')
    without_records = [item for item in address_dict.items() if item[1] is None]
    size = min(extract_size, len(without_records))
    print(f'Total records w/o google coordinates: {len(without_records)}\nStarting download of: {size} records')

    i = 0
    for i, record in enumerate(without_records):
        if i == size:
            break
        raw_address = record[0]
        g_address = rate_limited_google_call(connector, raw_address)
        address_dict[raw_address] = g_address

    print(f'Addresses downloaded: {i}\nItems left: {len(without_records) - i}')


if __name__ == '__main__':
    file_path = r'dict.risk.addresses'
    address_dict = load_object(file_path)
    download_maps_data(address_dict, 100)
    save_object(address_dict, file_path)
    # pass