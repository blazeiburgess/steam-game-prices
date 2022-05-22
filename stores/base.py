import logging
from utils import random_sleep
from file_handlers import CSVWriter
from datetime import datetime

class BaseStore(object):
    PullerClass = None
    ParserClass = None
    FileWriterClass = CSVWriter

    store_name = None
    default_max_offset = None
    results = []
    unique_keys = []
    unique_key = None
    def __init__(self, cli_args, *args, **kwargs):
        self.args = cli_args
        self.log = logging.getLogger(self.__class__.__name__)
        self.pull_timestamp = int(datetime.timestamp(datetime.utcnow()))

        if cli_args['max_offset'] == -1:
            self.log.info(f'Default max offset will be used: {self.default_max_offset}')
            cli_args['max_offset'] = self.default_max_offset

        self._puller = self.PullerClass(**cli_args)

        self.initialize(*args, **kwargs)


    def fill_results(self) -> list:
        """
        Generic way to get results by sending puller results to the parser. 
        Assumes a very specific implementation of both puller and parser.
        """
        for response in self._puller.pull():
            try:
                parser = self.ParserClass(response)
            except ParserError as pe:
                self.log.warning('Empty html page was found so etree couldn\'t parse it. Assuming there are no more results in the pull')
                break
            if self.unique_key:
                for parser_result in parser.parse():
                    if parser_result[self.unique_key] in self.unique_keys:
                        continue
                    else:
                        self.unique_keys.append(parser_result[self.unique_key])
                        self.results.append(parser_result)
            else:
                self.results.extend(
                        parser.parse()
                    )

            if self.args['skip_random_sleep'] == False:
                random_sleep(self.args['random_sleep_min'], self.args['random_sleep_max'])


        return self.results

    def write_results(self):
        if self.store_name is None:
            raise ValueError(f'Class attribute "store_name" cannot be None')

        writer = self.FileWriterClass(
                self.results,
                self.results[0].keys(),
                self.store_name,
                self.args['page_type'],
                self.pull_timestamp,
                self.args['operating_system'],
                self.args['query'],
                self.args['tags'],
                self.args['country_code'],
            )
        writer.write()


    def initialize(self, *args, **kwargs):
        pass
