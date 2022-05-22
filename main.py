from args import ArgParser
from pullers import SteamPuller
from parsers import SteamParser
from utils import random_sleep
from datetime import datetime
from file_handlers import CSVWriter
from constants import steam_tags, steam_countries
from enums import StoreEnum
import logging
from lxml.etree import ParserError

def main():
    argparser = ArgParser()
    args = argparser.parse()
    if args['game_store'] == StoreEnum.STEAM.value:
        from stores import SteamStore as Store
    elif args['game_store'] == StoreEnum.GOG.value:
        from stores import GogStore as Store
    else:
        raise ValueError(f'Store not supported: {args["game_store"]}')

    store = Store(args)
    store.run()


if __name__ == '__main__':
    main()
