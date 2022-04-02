from abc import ABC, abstractmethod


class Location(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class AddressLocation(Location):

    def __init__(self, address, category: str, incomplete=False):
        self.address = address
        self.category = category
        self.incomplete = incomplete

    def get_info(self):
        return {'address': self._address, 'category': self.category, 'incomplete': self.incomplete}

    @abstractmethod
    def __repr__(self):
        pass

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value: str):
        if value.isspace() or type(value) != str:
            raise ValueError('Address must be a string value of minimum 3 chars')
        self._address = value


class ResidentialAddress(AddressLocation):

    def __init__(self, address: str, incomplete=False) -> None:
        super().__init__(address, 'residential', incomplete)

    def __repr__(self):
        return f'ResidentialAddress("{self.address}")'


class PermanentAddress(AddressLocation):

    def __init__(self, address: str, incomplete=False) -> None:
        super().__init__(address, 'permanent', incomplete)

    def __repr__(self):
        return f'PermanentAddress("{self.address}")'


class GeoCoordinates(Location):

    def __init__(self, latitude: float, longitude) -> None:
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


if __name__ == "__main__":
    p_address = PermanentAddress('22 Permanent str., Sofia')
    r_address = ResidentialAddress('11 Residential str., Sofia')
    gc = GeoCoordinates(13.1111, 15.65498)

    print(p_address.get_info())
    print(p_address)
    print(r_address.get_info())

    print(gc.get_info())
    print(gc)
