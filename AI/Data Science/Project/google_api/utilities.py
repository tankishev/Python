from sklearn.cluster import DBSCAN
import numpy as np
import pickle


def haversine_distance(lat_a: float, lng_a: float, lat_b: float, lng_b: float, units='km'):
    """
    Calculates the haversine distance between two points given their coordinates.
    Default output is in km. Use 'units=m' for meters.

    :param lat_a: Latitude of point A
    :param lng_a: Longitude of point A
    :param lat_b: Latitude of point B
    :param lng_b: Longitude of point B
    :param units: Select 'm' or 'km' as units to measure distance
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

    :param coordinates: Iterable object with pairs of latitude and longitude coordinates.
    :param center_point: Latitude and longitude of the center point.
    :param radius: max distance in units to the center point for filter to return TRUE else returns FALSE
    :param units: Select 'm' or 'km' as units to measure distance
    """
    f = np.vectorize(haversine_distance)
    lat_a, lng_a = center_point
    lat_b = np.array([el[0] for el in coordinates])
    lng_b = np.array([el[1] for el in coordinates])
    result = f(lat_a, lng_a, lat_b, lng_b, units)

    return tuple(el <= radius for el in result)


def get_dbscan_clusters(coordinates: iter, min_cluster_size: int, distance: float, units='km', verbose=False):
    """ Generates a list of clusters using the DBSCAN algorithm, given:

    :param coordinates: an iterable with coordinates in the format (lat, lng)
    :param min_cluster_size: number of points required to define a cluster
    :param distance: radius distance between core points required to define a cluster
    :param units: set distance units; default is "km", use 'units="m"' for meters
    :param verbose: use 'True' to print out statistics on the console
    :return: None
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


def save_addr_obj(obj: dict, filename: str) -> None:
    """ Save pickle object

    :param obj: Object to save
    :param filename: Filename to use
    :return: None
    """
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)


def load_addr_obj(file_path: str) -> dict:
    """ Load pickle object

    :param file_path: Filename to use
    :return: Object
    """
    try:
        with open(file_path, 'rb') as file:
            data_object = pickle.load(file)
            return data_object
    except FileNotFoundError:
        return None
