from abc import ABC, abstractmethod
from DataObjects.utilities import load_object


class DataObject(ABC):

    def __init__(self, file_path) -> None:
        self.collection = None
        self.file_path = file_path
        self.__collection_index = 0

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value: str):
        if value.isspace() or value is None:
            raise ValueError("Path cannot be an empty string")
        self.__file_path = value

    def load_data(self) -> None:
        self.collection = load_object(self.file_path)

    @abstractmethod
    def filter(self, **kwargs):
        pass

    @classmethod
    def __from_filter(cls, path: str, observation_list: list) -> object:
        new_object = cls(path)
        new_object.collection = [el for el in observation_list]
        return new_object

    def __iter__(self) -> iter:
        self.__collection_index = 0
        return self

    def __next__(self):
        if self.__collection_index < len(self.collection):
            self.__collection_index += 1
            return self.collection[self.__collection_index - 1]
        raise StopIteration()

    def __len__(self):
        return len(self.collection)

    def __getitem__(self, item):
        return self.collection[item]


class CreditObservations(DataObject):

    def __init__(self, file_path) -> None:
        super().__init__(file_path)

    @property
    def coordinates(self):
        return [el.coordinates for el in self.collection]

    @property
    def coordinates_reversed(self):
        return [el.coordinates_reversed for el in self.collection]

    def filter(self, **kwargs):
        filters = {
            'creditid': lambda item: True if 'creditid' not in kwargs.keys() else (item in kwargs.get('creditid', [])),
            'is_bad': lambda item: True if 'is_bad' not in kwargs.keys() else item == kwargs.get('is_bad'),
            'g_data': lambda item: True if 'g_data' not in kwargs.keys() else item == kwargs.get('g_data'),
            'g_status': lambda item: True if 'g_status' not in kwargs.keys() else item == kwargs.get('g_status'),
            'country': lambda item: True if 'country' not in kwargs.keys() else item == kwargs.get('country')
        }

        def g_status(google_address):
            if google_address:
                return google_address.geocoding_data.get('status', None)

        def g_country(google_address):
            if google_address:
                if google_address.address_components:
                    return google_address.address_components.get('country', None)

        filtered_list = [el for el in self.collection if
                         filters['is_bad'](el.credit.bad_flag)
                         and filters['creditid'](el.credit.creditid)
                         and filters['g_data']((el.google_address is not None))
                         and filters['g_status'](g_status(el.google_address))
                         and filters['country'](g_country(el.google_address))]

        if kwargs.get('exclude', False) is True:
            filtered_list = [el for el in self.collection if el not in filtered_list]

        return self.__from_filter(self.file_path, filtered_list)

