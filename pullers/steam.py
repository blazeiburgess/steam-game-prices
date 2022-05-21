from constants import steam_tags
from .base import BasePuller
class SteamPuller(BasePuller):
    PULL_URL_TEMPLATE = 'https://store.steampowered.com/search/results/?query={query}&start={offset}&tags={tags}&count=50&filter={page_type}&dynamic_data=&sort_by=_ASC&infinite=1&cc={cc}&os={os}'
    base_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
        }
    def initialize(self, query, tags, operating_system, page_type, starting_offset, max_offset, country_code, *args, **kwargs):
        self.mapped_tags = []
        self.query = query
        self.operating_system = operating_system
        self.page_type = page_type
        self.starting_offset = starting_offset
        self.max_offset = max_offset
        self.country_code = country_code
        if tags:
            for tag in tags:
                self.mapped_tags.append(
                        steam_tags[tag]
                    )

    def pull(self):
        for offset in range(self.starting_offset, self.max_offset, 50):
            url = self.PULL_URL_TEMPLATE.format(
                    query=self.query,
                    offset=offset,
                    os=self.operating_system or '',
                    page_type=self.page_type,
                    tags=",".join(self.mapped_tags),
                    cc=self.country_code,
                )
            self.log.info(f"Pulling url: {url}")
            page = self._get(url)
            resp = page.json()
            raw_html = resp['results_html']
            yield raw_html

