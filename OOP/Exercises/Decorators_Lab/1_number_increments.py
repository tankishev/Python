def number_increment(numbers: list) -> list:
    def increase():
        return [x + 1 for x in numbers]
    return increase()
