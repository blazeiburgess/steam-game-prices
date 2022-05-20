from .base import BaseEnum

class SteamPageType(BaseEnum):
    TOP = 'topsellers'
    NEW = 'newreleases'
    UPCOMING = 'upcoming'

class SteamOperatingSystem(BaseEnum):
    WINDOWS = 'win'
    LINUX = 'linux'
    OSX = 'mac'
