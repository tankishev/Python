class AIBC:
    """
    This is an Auto Incrementable Base Class (AIBC) that generates
    auto incrementing id for each instance
    """

    id = 1

    def __init__(self) -> None:
        self.id = self.__class__.get_next_id()

    @classmethod
    def get_next_id(cls) -> int:
        cls.id += 1
        return cls.id - 1
