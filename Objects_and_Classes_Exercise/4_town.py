# Create a class Town. The __init__ method should receive the name of the town (string). 
# Each town has a latitude - "0°N" upon initialization and a longitude - "0°E" upon initialization. 
# It should also have 3 more methods:
# •	set_latitude(latitude) - sets an latitude
# •	set_longitude(longitude) - sets an longitude
# •	__repr__ - returns a representation of the object in the following string format:
# "Town: {name} | Latitude: {latitude} | Longitude: {longitude}"

class Town:
    def __init__(self, name: str) -> None:
        self.name = name
        self.latitude = '0°N'
        self.longitude = '0°E' 

    def set_latitude(self, latitude) -> None:
        self.latitude = latitude

    def set_longitude(self, longitude) -> None:
        self.longitude = longitude

    def __repr__(self) -> str:
        return f'Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}'

# Test code
town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
