from abc import ABC, abstractmethod
from urllib.parse import urlencode
import requests


class GoogleAPIConnection(ABC):
    _API_KEY = 'AIzaSyDjhK-fLqzRNumGtL9B1It5jXN6lxytkio'

    @abstractmethod
    def __init__(self):
        pass


class GeocodingAPI(GoogleAPIConnection):
    __DATA_TYPES = ['json']
    __SERVER = 'https://maps.googleapis.com/maps/api/geocode/'
    __OPTIONAL_PARAMETERS = ['region']

    def __init__(self, data_type: str) -> None:
        self.data_type = data_type

    @property
    def data_type(self):
        return self._data_type
    
    @data_type.setter
    def data_type(self, value):
        if value not in self.__DATA_TYPES:
            raise ValueError(f'Allowed connection types: {self.__DATA_TYPES}')
        self._data_type = value

    def get_location_data(self, address, **kwargs):
        params = {'address': address, 'key': self._API_KEY}
        for key, value in kwargs.items():
            if key in self.__OPTIONAL_PARAMETERS:
                params[key] = value

        url_params = urlencode(params)
        endpoint = f'{self.__SERVER}{self.data_type}'
        url = f'{endpoint}?{url_params}'
        r = requests.get(url)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()

    @staticmethod
    def extract_coordinates(location_data: dict):
        try:
            result = location_data['results'][0]['geometry']['location']
            return result
        except:
            pass
