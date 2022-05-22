from constants import steam_tags
from .base import BasePuller
class GogPuller(BasePuller):
    PULL_URL_TEMPLATE = 'https://catalog.gog.com/v1/catalog?limit=48&order=desc%3Atrending&productType=in%3Agame%2Cpack%2Cdlc%2Cextras&page={page}&countryCode={cc}&query={query}&systems={os}&tags={tags}'
    base_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
        }

    OS_MAPPER = {
            'mac': 'osx',
            'linux': 'linux',
            'win': 'windows'
        }
    def initialize(self, query, tags, operating_system, page_type, starting_offset, max_offset, country_code, *args, **kwargs):
        self.page_type = page_type
        self.starting_offset = starting_offset
        self.max_offset = max_offset
        self.country_code = country_code

        self.tags = f'is:{",".join(tags)}' if tags else ''
        self.operating_system = f'in:{self.OS_MAPPER.get(operating_system)}' if operating_system else ''

        if query:
            self.query = f'like:{query}'
        else:
            self.query = ''


    def pull(self):
        for page in range(self.starting_offset, self.max_offset):
            url = self.PULL_URL_TEMPLATE.format(
                    query=self.query,
                    page=page,
                    os=self.operating_system,
                    page_type=self.page_type,
                    tags=self.tags,
                    cc=self.country_code,
                )
            self.log.info(f"Pulling url: {url}")
            page = self._get(url)
            resp = page.json()
            yield resp

