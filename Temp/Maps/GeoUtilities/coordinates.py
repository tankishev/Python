from GeoUtilities.location import Location


class GeoCoordinates(Location):

    def __init__(self, latitude: float, longitude: float) -> None:
        self.latitude = latitude
        self.longitude = longitude

    def get_info(self) -> dict:
        return {'lat': self.latitude, 'lng': self.longitude}

    def __repr__(self):
        return f'GeoCoordinates({self.latitude}, {self.longitude})'

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if value < -90 or value > 90:
            raise ValueError('Latitude must between -90 and 90')
        self._latitude = value

    @ property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if value < -180 or value > 180:
            raise ValueError('Longitude must between -180 and 180')
        self._longitude = value
