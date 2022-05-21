from .html import HTMLParser
from utils import parse_float

class SteamParser(HTMLParser):
    def _remove_empty_values(self, results: list) ->list:
        return [val.strip() for val in results if val.strip()]

    def _get_clean_price_values(self, results: list) -> str:
        clean_results = self._remove_empty_values(results)
        if results and clean_results:
            if len(clean_results) == 1:
                return None, clean_results[0], None
            elif len(clean_results) == 2:
                return None, clean_results[0], clean_results[1]
            elif len(clean_results) == 3:
                return clean_results[0], clean_results[1], clean_results[2]
            else:
                raise ValueError(f'More results than expected: {clean_results}')
        else:
            raise ValueError(f"No results or clean results: {results}")



    def parse(self):
        records = []
        for row in self.etree.xpath("//a[contains(@class,'search_result_row')]"):
            results = row.xpath('.//text()')
            try:
                discount, price, discounted_price = self._get_clean_price_values(row.xpath('.//div[contains(@class,"search_price")]//text()'))
            except ValueError as ve:
                self.log.warning(f"Could not find price in row: {[rec.strip() for rec in results if rec.strip()]}")
                continue
            try:
                parsed_price = parse_float(price)
            except:
                self.log.warning(f'Failed to parse price, so setting parsed value to None: {price}')
                parsed_price = None

            url = row.xpath('@href')[0].strip().split('?')[0]
            app_id = url.split('/app/')[-1].split('/')[0] if '/app/' in url else None
            bundle_id = url.split('/bundle/')[-1].split('/')[0] if '/bundle/' in url else None
            try:
                release_date = self._remove_empty_values(row.xpath('.//div[contains(@class,"search_released")]/text()'))[0]
            except IndexError as ie:
                self.log.warning(f"Could not find release_date in row: {[rec.strip() for rec in results if rec.strip()]}")
                release_date = None
            record = {
                    'app_id': app_id,
                    'title': self._remove_empty_values(row.xpath('.//*[@class="title"]/text()'))[0],
                    'release_date': release_date,
                    'discount': discount,
                    'price': price,
                    'parsed_price': parsed_price,
                    'discounted_price': discounted_price,
                    'bundle_id': bundle_id,
                    'url': url,
            }
            records.append(record)
        return records
