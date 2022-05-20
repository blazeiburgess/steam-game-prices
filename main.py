from args import ArgParser
from pullers import SteamPuller
from parsers import SteamParser
from utils import random_sleep
def main():
    argparser = ArgParser()
    args = argparser.parse()
    if args['tags']:
        args['tags'] = set(args['tags'])
    puller = SteamPuller(**args)
    for raw_html_page in puller.pull():
        page_parser = SteamParser(raw_html_page)
        results = page_parser.parse()

        random_sleep(args['random_sleep_min'], args['random_sleep_max'])
    print(args)

if __name__ == '__main__':
    main()
