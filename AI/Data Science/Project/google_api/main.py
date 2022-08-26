from utilities import save_addr_obj, load_addr_obj
from ratelimit import RateLimiter
from googe_geocoding import GeocodingAPI


def download_maps_data(addr_dict: dict, extract_size=200, verbose=False) -> int:
    """Downloads data from Google GeoCodingAPI and stores it in the provided dictionary

    :param addr_dict: Dictionary with RAW addresses for which GeoCoding data has to be downloaded.
    :param extract_size: number of records to extract.
    :param verbose: Boolean flag for console printing
    :return: Number of records downloaded.
    """

    @RateLimiter(10, 1)
    def rate_limited_google_call(conn, address):
        retval = conn.get_location_data(address, region='BG')
        return retval

    # set_up
    connector = GeocodingAPI('json')
    without_records = [item for item in addr_dict.items() if item[1] is None]
    size = min(extract_size, len(without_records))
    if verbose:
        print(f'Total records w/o google coordinates: {len(without_records)}\nStarting download of: {size} records')

    i = 0
    for i, record in enumerate(without_records):
        if i == size:
            break
        raw_address = record[0]
        g_address = rate_limited_google_call(connector, raw_address)
        if raw_address not in addr_dict.keys():
            addr_dict[raw_address] = []
        addr_dict[raw_address] = g_address

    if verbose:
        print(f'Addresses downloaded: {i}\nItems left: {len(without_records) - i}')

    return i


if __name__ == '__main__':
    file_path = r'../data/dict.json.loans.addr'
    address_dict = load_addr_obj(file_path)
    download_maps_data(address_dict, 2000, verbose=True)
    save_addr_obj(address_dict, file_path)



