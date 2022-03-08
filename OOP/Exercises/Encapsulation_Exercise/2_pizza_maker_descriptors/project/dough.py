from .data_descriptors import PositiveNum, NonEmptyString


class Dough:

    flour_type = NonEmptyString('The flour type cannot be an empty string')
    baking_technique = NonEmptyString('The baking technique cannot be an empty string')
    weight = PositiveNum('The weight cannot be less or equal to zero')

    def __init__(self, flour_type: str, baking_technique: str, weight: float) -> None:
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight
