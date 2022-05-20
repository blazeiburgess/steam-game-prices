from enum import Enum
class BaseEnum(Enum):
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def choice_values(cls):
        return [key.value for key in cls]
