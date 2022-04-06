from google_api_connection import GoogleAPIConnection
from urllib.parse import urlencode
from Temp.Maps.DataObjects.locations import Location
import requests


class GoogleAddress(Location):

    def __init__(self, geocoding_data: dict) -> None:
        self.geocoding_data = geocoding_data

    def get_info(self):
        status = self.geocoding_data.get('status', None)
        if status != 'OK':
            return {'status': status}
        retval = dict()
        retval['location'] = self.coordinates
        retval['formatted_address'] = self.formatted_address
        retval['address_components'] = self.address_components
        return retval

    @property
    def coordinates(self):
        status = self.geocoding_data.get('status', None)
        if status == 'OK':
            return self.geocoding_data['results'][0].get('geometry', None).get('location', None)

    @property
    def formatted_address(self):
        return self.geocoding_data['results'][0].get('formatted_address', None)

    @property
    def address_components(self):
        retval = dict()
        results = self.geocoding_data.get('results', None)
        if results:
            address_data = results[0].get('address_components', None)
            for el in address_data:
                retval[el['types'][0]] = el.get('long_name', None)
            return retval

    def __repr__(self):
        return f'GoogleAddress({self.geocoding_data})'


class GeocodingAPI(GoogleAPIConnection):
    __DATA_TYPES = ['json']
    __SERVER = 'https://maps.googleapis.com/maps/api/geocode/'
    __OPTIONAL_PARAMETERS = ['region']

    def __init__(self, data_type: str) -> None:
        self.data_type = data_type
        self.__buffer = None

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
        self.__buffer = r.json()
        return r.json()

    def get_address(self) -> GoogleAddress:
        if not self.__buffer:
            raise ValueError('Buffer empty. Use get_location_data() first')
        return GoogleAddress(self.__buffer)
