import argparse
from enums import SteamPageType
from constants import steam_tags

PAGE_TYPE_HELP_TEXT = f"""You have a choice of page type to pull from. Options for Steam are:
    '{"', '".join(SteamPageType.choice_values())}'

"""

class ArgParser(object):
    def __init__(self):
        self._parser = argparse.ArgumentParser(description="This application pulls price and deal data from the steam store")

    def set_args(self):
        # self._parser.add_argument(
        #         '--store', type=str.lower, dest='store',
        #         default='steam', help="Unused. This specifies the store, but we currently only supports Steam"
        #     )
        self._parser.add_argument(
                '--page-type', type=str.lower,
                dest='page_type', help=PAGE_TYPE_HELP_TEXT,
                default='topsellers', choices=SteamPageType.choice_values(), metavar=''
            )
        self._parser.add_argument(
                '--starting-offset', type=int,
                dest='starting_offset', help="Initial offset on results. Offset is by items, not page. Default: 0",
                default=0
            )
        self._parser.add_argument(
                '--max-offset', type=int,
                dest='max_offset', help="Max offset on results. Offset is by items, not page. Default: 500",
                default=500
            )
        self._parser.add_argument(
                '--query', '-q', type=str, default='',
                dest='query', help='Optional query to filter results. This is equivalent to using the search bar in Steam'
            )

        self._parser.add_argument(
                '--operating-system', '--os', type=str.lower, default='',
                dest='operating_system', help='Optional filter on operating system'
            )
        self._parser.add_argument(
                '--tag','-t', action='append', type=lambda s: s.lower().replace('_',' '), 
                dest='tags', help='Optional tags to filter results. This is equivalent to using the filters in Steam. tags are case insensitive and you can use spaces or underscores (_) interchangably',
                choices=sorted(steam_tags.keys()), metavar=''
            )
        self._parser.add_argument(
                '--skip-random-sleep','--no-random-sleep', action='store_true', 
                default=False, dest='skip_random_sleep',
                help="This will stop the program from sleeping for a pseudo-random period of time after each page pull"
            )
        self._parser.add_argument(
                '--user-agent', '--ua', type=str, default='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
                dest='user_agent', help='The User-Agent used in request headers for each page pull. Defaults to Chrome v101 on Windows 10.'
            )
        self._parser.add_argument(
                '--random-sleep-min','--rs-min', type=int, default=0,
                dest='random_sleep_min',
                help="Minimum amount of time in seconds spent sleeping between requests. Ignored if '--skip-random-sleep' flag is set. Default: 0"
            )
        self._parser.add_argument(
                '--random-sleep-max','--rs-max', type=int, default=4,
                dest='random_sleep_max',
                help="Maximum amount of time in seconds spent sleeping between requests. Ignored if '--skip-random-sleep' flag is set. Deafult: 4"
            )
        

    def _validate_args(self, args):
        if not args['skip_random_sleep'] and args['random_sleep_min'] > args['random_sleep_max']:
            raise ValueError('Minimum random sleep value ({random_sleep_min}) cannot be higher than maximum ({random_sleep_max})'.format(**args))
        return args
            
    def parse(self):
        self.set_args()
        args, remaning = self._parser.parse_known_args()
        return self._validate_args(vars(args))