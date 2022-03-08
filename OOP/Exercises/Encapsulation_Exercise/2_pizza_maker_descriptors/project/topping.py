from .data_descriptors import PositiveNum, NonEmptyString


class Topping:

    topping_type = NonEmptyString('The topping type cannot be an empty string')
    weight = PositiveNum('The weight cannot be less or equal to zero')

    def __init__(self, topping_type: str, weight: float) -> None:
        self.topping_type = topping_type
        self.weight = weight
