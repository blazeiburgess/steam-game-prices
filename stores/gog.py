from .base import BaseStore

from pullers import GogPuller
from parsers import GogParser

from constants import gog_tags

class GogStore(BaseStore):
    PullerClass = GogPuller
    ParserClass = GogParser
    store_name = 'gog'
    default_max_offset = 5
    unique_key = 'slug'

    def initialize(self, *args, **kwargs):
        pass

    def run(self) -> list or None:
        if self.args['list_tags'] is True:
            return print("\n".join(
                sorted(
                    [tag['slug'] for tag in gog_tags]
                )
            ))

        if self.args['tags']:
            self.args['tags'] = set(self.args['tags'])

        self.fill_results() # this comes from the base class
        self.write_results()
