# Create a base class Vehicle. It should contain the following attributes:
# •	DEFAULT_FUEL_CONSUMPTION: float (constant)
# •	fuel_consumption: float – the given fuel consumption is per kilometer
# •	fuel: float – represent the fuel in the specific vehicle
# •	horse_power: int
# The class should receive fuel and horse_power upon initialization and should set the default fuel consumption on the
# attribute fuel_consumption.
# The class should have the following methods:
# •	drive(kilometers) - reduces the fuel based on the travelled kilometers and fuel consumption.
# Keep in mind that you can drive the vehicle only if you have enough fuel to finish the driving.
# The default fuel consumption for Vehicle is 1.25. Some classes have different default fuel consumption:
# •	SportCar - 10
# •	RaceMotorcycle - 8
# •	Car - 3

from project.vehicle import Vehicle
from project.family_car import FamilyCar


vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)
