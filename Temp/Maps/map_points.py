import numpy as np


class MapPoint:

    def __init__(self, address: str) -> None:
        self.address = address
        self._latitude = None
        self._longitude = None

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

    def get_distance(self, other_point) -> float:
        if not self._longitude or not self._latitude:
            raise ValueError('MapPoint coordinates not set')
        if other_point.__class__.__name__ != self.__class__.__name__:
            raise TypeError(f'Parameter should be of type {self.__class__.__name__}')
        if other_point.longitude is None or other_point.latitude is None:
            raise ValueError('Passed MapPoint object does not have its coordinates set')

        latitude_a = self.latitude * np.pi / 180
        latitude_b = other_point.latitude * np.pi / 180
        delta_latitude = (other_point.latitude - self.latitude) * np.pi / 180
        delta_longitude = (other_point.longitude - self.longitude) * np.pi / 180

        raw_result = np.sin(delta_latitude / 2) ** 2 \
            + np.sin(delta_longitude / 2) ** 2 \
            * np.cos(latitude_a) * np.cos(latitude_b)

        raw_result = 2 * np.arctan2(np.sqrt(raw_result), np.sqrt(1-raw_result))

        result = raw_result * 6371
        return result

    @classmethod
    def from_coordinates(cls, latitude: float, longitude: float):
        new_point = MapPoint('None')
        new_point.latitude = latitude
        new_point.longitude = longitude
        return new_point