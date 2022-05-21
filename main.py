from args import ArgParser
from pullers import SteamPuller
from parsers import SteamParser
from utils import random_sleep
from datetime import datetime
from file_handlers import CSVWriter
from constants import steam_tags, steam_countries
import logging
from lxml.etree import ParserError

def main():
    log = logging.getLogger('__main__')
    argparser = ArgParser()
    args = argparser.parse()
    if args['list_steam_tags'] is True:
        return print("\n".join(
            sorted(
                [key.replace(' ','_') for key in steam_tags.keys()]
            )
        ))
    if args['list_steam_countries'] is True:
        lines = []
        for country in sorted(steam_countries, key=lambda x: x['code']):
            lines.append("{code}   | {name}".format(**country))
        print("ISO2 | Name\n----------------------")
        return print("\n".join(lines))
    if args['tags']:
        args['tags'] = set(args['tags'])

    pull_timestamp = int(datetime.timestamp(datetime.utcnow()))

    puller = SteamPuller(**args)
    results = []
    for raw_html_page in puller.pull():
        try:
            page_parser = SteamParser(raw_html_page)
        except ParserError as pe:
            log.warning("Empty html page was returned from puller. Assuming there are no more results to pull")
            break
        results.extend(page_parser.parse())

        random_sleep(args['random_sleep_min'], args['random_sleep_max'])

    writer = CSVWriter(results, results[0].keys(), 'steam', args['page_type'], pull_timestamp, args['operating_system'],
            args['query'], args['tags'])
    writer.write()

if __name__ == '__main__':
    main()
