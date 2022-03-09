class Integer:

    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if isinstance(float_value, float):
            return cls(int(float_value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, value: str):
        return cls(Integer.roman_to_int(value))

    @staticmethod
    def roman_to_int(roman: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_val = 0
        for i in range(len(roman)):
            next_val = roman_dict.get(roman[i], 0)
            if next_val < max([roman_dict[el] for el in roman[i:]]):
                next_val *= -1
            roman_val += next_val
        return roman_val

    @classmethod
    def from_string(cls, value: str):
        if isinstance(value, str) and value.isnumeric():
            return cls(int(value))
        return "wrong type"


# Test case
if __name__ == '__main__':
    first_num = Integer(10)
    print(first_num.value)

    second_num = Integer.from_roman("IV")
    print(second_num.value)

    print(Integer.from_float("2.6"))
    print(Integer.from_string(2.6))
