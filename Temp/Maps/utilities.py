import pickle
import numpy as np
import datetime as dt


def save_object(object_to_save: object, filename: str) -> object:
    with open(filename, 'wb') as file:
        pickle.dump(object_to_save, file)


def read_object_from_file(filename):
    try:
        with open(filename, 'rb') as file:
            read_object = pickle.load(file)
        return read_object
    except FileNotFoundError:
        return None


def calc_distance(lat_a, lng_a, lat_b, lng_b):
    latitude_a = lat_a * np.pi / 180
    latitude_b = lat_b * np.pi / 180
    delta_latitude = (lat_b - lat_a) * np.pi / 180
    delta_longitude = (lng_b - lng_a) * np.pi / 180

    raw_result = np.sin(delta_latitude / 2) ** 2 \
                 + np.sin(delta_longitude / 2) ** 2 \
                 * np.cos(latitude_a) * np.cos(latitude_b)

    raw_result = 2 * np.arctan2(np.sqrt(raw_result), np.sqrt(1 - raw_result))

    result = raw_result * 6371
    return result


def print_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = dt.datetime.now()
        func(*args, **kwargs)
        duration = (dt.datetime.now() - start_time).total_seconds()
        print(f'Execution time: {duration}s')
    return wrapper
