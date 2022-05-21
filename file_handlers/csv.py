from csv import DictWriter
from utils import parse_float
class CSVWriter(object):
    def __init__(self, data: dict, fieldnames: list, store: str, page_type: str, timestamp: int, operating_system: str, 
            query: str, tags: list, country_code: str, *args, output_location: str='output', **kwargs):
        self.data = sorted(
                data, 
                key=lambda x: ( # TODO: make sort function controllable by user
                    int(
                        str(x['discount'] or '0').replace('%','').replace('-','')
                    ),
                    parse_float(x['price']), 
                ),
                # key=lambda x: (
                #     x['parsed_price'] - parse_float(str(x['discounted_price'] or x['price'])),
                #     x['parsed_price'], 
                # ),
                reverse=True
            )
        self.fieldnames = fieldnames


        #TODO: make filename structure an argument
        if operating_system:
            os = f'{operating_system}_'
        else:
            os = ''
        if query:
            query = f'{query}_'
        else:
            query = ''
        if country_code:
            country_code = f'{country_code}_'
        else:
            country_code = ''

        if tags:
            tags = "--".join(list(tags)[:4]).replace(' ','_') + '_'
        else:
            tags = ''

        self.filename = f'{output_location}/{store}_{os}{country_code}{page_type}_{query}{tags}{timestamp}.csv'


    def write(self):
        with open(self.filename, 'w') as f:
            writer = DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(self.data)
        return self.filename
