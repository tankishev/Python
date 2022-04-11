from Temp.Maps.GeoUtilities.location import AddressLocation
from Temp.Maps.DataObjects.credit import Credit


class Observation:

    def __init__(self, credit: Credit, address: AddressLocation) -> None:
        self.credit = credit
        self.address = address
        self.google_address = None

    def get_info(self):
        return f'Credit: {self.credit.get_info()}\n' \
               f'Address: {self.address.get_info()}\n' \
               f'GoogleInfo: {self.google_address.get_info()}'

    @property
    def coordinates(self):
        if self.google_address:
            google_coordinates = self.google_address.coordinates
            if google_coordinates:
                return google_coordinates['lat'], google_coordinates['lng']

    @property
    def coordinates_reversed(self):
        if self.google_address:
            google_coordinates = self.google_address.coordinates
            if google_coordinates:
                return google_coordinates['lng'], google_coordinates['lat']

