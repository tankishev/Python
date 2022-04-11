import pickle
import datetime as dt


def save_object(object_to_save: object, filename: str) -> None:
    with open(filename, 'wb') as file:
        pickle.dump(object_to_save, file)


def load_object(file_path: str):
    try:
        with open(file_path, 'rb') as file:
            data_object = pickle.load(file)
            return data_object
    except FileNotFoundError:
        return None


def print_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = dt.datetime.now()
        func(*args, **kwargs)
        duration = (dt.datetime.now() - start_time).total_seconds()
        print(f'Execution time: {duration}s')
    return wrapper




