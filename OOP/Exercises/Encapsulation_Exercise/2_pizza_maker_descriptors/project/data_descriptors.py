class PositiveNum:

    def __init__(self, error_message: str):
        self.error_message = error_message

    def __set_name__(self, owner, name):
        self.attr_name = '__' + name

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(self.error_message)
        instance.__dict__[self.attr_name] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.attr_name, None)


class NonEmptyString:

    def __init__(self, error_message: str):
        self.error_message = error_message

    def __set_name__(self, owner, name):
        self.attr_name = '__' + name

    def __set__(self, instance, value):
        if value == '':
            raise ValueError(self.error_message)
        instance.__dict__[self.attr_name] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.attr_name, None)
