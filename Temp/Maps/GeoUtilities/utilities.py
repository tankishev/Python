from sklearn.cluster import DBSCAN
import numpy as np
import re


def haversine_distance(lat_a: float, lng_a: float, lat_b: float, lng_b: float, units='km'):
    """
    Calculates the haversine distance between two points given their coordinates.
    Default output is in km. Use 'units=m' for meters
    """
    units_dict = {
        'km': 1,
        'm': 1000
    }

    latitude_a = lat_a * np.pi / 180
    latitude_b = lat_b * np.pi / 180
    delta_latitude = (lat_b - lat_a) * np.pi / 180
    delta_longitude = (lng_b - lng_a) * np.pi / 180

    raw_result = np.sin(delta_latitude / 2) ** 2 \
        + np.sin(delta_longitude / 2) ** 2 \
        * np.cos(latitude_a) * np.cos(latitude_b)

    raw_result = 2 * np.arctan2(np.sqrt(raw_result), np.sqrt(1 - raw_result))

    result = raw_result * 6371.0088 * units_dict.get(units, 1)
    return result


def radius_filter(coordinates: iter, center_point: tuple, radius: float, units='km') -> tuple:
    """
    Filters a given list based on distance to a center point.
    'coordinates' and 'center_point' should be in a ('lat', 'lng') format
    Default radius distance is in km. Use 'units=m' for meters.
    Returns a True/False filtered tuple
    """
    f = np.vectorize(haversine_distance)
    lat_a = center_point[0]
    lng_a = center_point[1]
    lat_b = np.array([el[0] for el in coordinates])
    lng_b = np.array([el[1] for el in coordinates])
    result = f(lat_a, lng_a, lat_b, lng_b, units)

    return tuple(el <= radius for el in result)


def google_address_filter(addresses: iter, reference_address) -> tuple:
    """
    Filters a given list of GoogleAddress objects based on matching 'address_components'
    to a reference GoogleAddress object.
    Returns a True/False filtered tuple.
    """
    result = []
    ref = reference_address.address_components
    ref_keys = set(ref.keys())
    for address in addresses:
        try:
            adr = address.address_components
            if ref_keys.issubset(set(adr.keys())):
                result.append(all(adr[key] == ref[key] for key in ref_keys))
            else:
                result.append(False)
        except:
            result.append(False)
    return tuple(el for el in result)


def get_dbscan_clusters(coordinates: iter, min_cluster_size: int, distance: float, units='km', verbose=False):
    """
    Generates a list of clusters using the DBSCAN algorithm, given:
    coordinates: iter - a list/tuple of coordinates in the format (lat, lng),
    min_cluster_size: int - number of points required to define a cluster
    distance: float - radius distance between core points required to define a cluster
    units="km" - default is "km", use 'units="m"' for meters
    verbose=False - use 'True' to print out statistics
    """
    units_dict = {
        'km': 1,
        'm': 1000
    }
    distance_per_radian = 6371.0088 * units_dict.get(units, 1)
    epsilon = distance / distance_per_radian

    x = np.radians(coordinates)
    db = DBSCAN(eps=epsilon, min_samples=min_cluster_size, algorithm='ball_tree', metric='haversine').fit(x)
    cluster_labels = db.labels_
    index_by_cluster = {}
    for i, cluster_id in enumerate(cluster_labels):
        if cluster_id != -1:
            if cluster_id not in index_by_cluster.keys():
                index_by_cluster[cluster_id] = []
            index_by_cluster[cluster_id].append(i)

    if verbose:
        n_noise = list(cluster_labels).count(-1)
        print(f'Data points: {len(x)}')
        print(f'Number of clusters: {len(index_by_cluster.keys())}')
        print(f'Number of cluster points: {len(x) - n_noise}')
        print(f'Number of noise points: {n_noise}')

    return index_by_cluster


def fix_address(address: str) -> str:
    """
    Removes any extra 0s from the address (e.g. street number ", 007").
    Returns None if address is None.
    Adds "БЪЛГАРИЯ" in front of each address if not None.
    """
    if address and address != 'NULL':
        address = address.upper().strip()
        retval = ''
        pattern = r'(\d+)'
        matches = re.finditer(pattern, address)

        i = 0
        for el in matches:
            retval += address[i:el.span()[0]] + str(int(el.group(1)))
            i = el.span()[1]
        if i > 0:
            retval += address[i:]

        if len(retval) > 0:
            return f'БЪЛГАРИЯ, {retval}'
        return f'БЪЛГАРИЯ, {address.upper().strip()}'
