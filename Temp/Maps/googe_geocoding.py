from google_api_connection import GoogleAPIConnection
from urllib.parse import urlencode
from locations import Location
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
        return self.geocoding_data['results'][0].get('geometry', None).get('location', None)

    @property
    def formatted_address(self):
        return self.geocoding_data['results'][0].get('formatted_address', None)

    @property
    def address_components(self):
        retval = dict()
        address_data = self.geocoding_data['results'][0].get('address_components', None)
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


# Review of the class
if __name__ == '__main__':
    temp_address = {'results': [{'address_components': [{'long_name': '15', 'short_name': '15', 'types': ['street_number']}, {'long_name': 'ulitsa "Zografski Manastir"', 'short_name': 'ul. "Zografski Manastir"', 'types': ['route']}, {'long_name': 'ж.к. Илинден', 'short_name': 'ж.к. Илинден', 'types': ['neighborhood', 'political']}, {'long_name': 'Sofia', 'short_name': 'Sofia', 'types': ['locality', 'political']}, {'long_name': 'Sofia City Province', 'short_name': 'Sofia City Province', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'Bulgaria', 'short_name': 'BG', 'types': ['country', 'political']}, {'long_name': '1309', 'short_name': '1309', 'types': ['postal_code']}], 'formatted_address': 'ul. "Zografski Manastir" 15, 1309 ж.к. Илинден, Sofia, Bulgaria', 'geometry': {'location': {'lat': 42.7058912, 'lng': 23.2928251}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 42.70727898029151, 'lng': 23.2940968802915}, 'southwest': {'lat': 42.70458101970851, 'lng': 23.2913989197085}}}, 'place_id': 'ChIJJYo2NU2FqkARXMgCkwgKCwA', 'plus_code': {'compound_code': 'P74V+94 Sofia', 'global_code': '8GJ5P74V+94'}, 'types': ['street_address']}], 'status': 'OK'}
    address = GoogleAddress(temp_address)
    print(address.get_info())
    print(address)
