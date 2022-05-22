from .base import BaseEnum


class CurrencyDisplay(BaseEnum):
    USD = '$'
    BRL = 'R$'

class StoreEnum(BaseEnum):
    STEAM = 'steam'
    GOG = 'gog'
