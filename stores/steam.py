from .base import BaseStore

from pullers import SteamPuller
from parsers import SteamParser

from constants import steam_tags, steam_countries

class SteamStore(BaseStore):
    PullerClass = SteamPuller
    ParserClass = SteamParser
    store_name = 'steam'
    default_max_offset = 250

    def initialize(self, *args, **kwargs):
        pass

    def run(self) -> list or None:
        if self.args['list_tags'] is True:
            return print("\n".join(
                sorted(
                    [key.replace(' ','_') for key in steam_tags.keys()]
                )
            ))
        if self.args['list_steam_countries'] is True:
            lines = []
            for country in sorted(steam_countries, key=lambda x: x['code']):
                lines.append("{code}   | {name}".format(**country))
            print("ISO2 | Name\n----------------------")
            return print("\n".join(lines))

        if self.args['tags']:
            self.args['tags'] = set(self.args['tags'])

        self.fill_results() # this comes from the base class
        self.write_results()
