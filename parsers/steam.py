from .html import HTMLParser

class SteamParser(HTMLParser):
    def _remove_empty_values(self, results: list) ->list:
        return [val.strip() for val in results if val.strip()]

    def _get_clean_value(self, results: list) -> str:
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



    def parse(self):
        records = []
        for row in self.etree.xpath("//a[contains(@class,'search_result_row')]"):
            discount, price, discounted_price = self._get_clean_value(row.xpath('.//div[contains(@class,"search_price")]//text()'))
            record = {
                    'url': row.xpath('@href')[0].strip(),
                    'title': self._remove_empty_values(row.xpath('.//*[@class="title"]/text()'))[0],
                    'discount': discount,
                    'price': price,
                    'discounted_price': discounted_price,
            }
            records.append(record)
        return records
