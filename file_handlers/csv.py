from csv import DictWriter
from utils import parse_float
class CSVWriter(object):
    def __init__(self, data: dict, fieldnames: list, store: str, page_type: str, timestamp: int, operating_system: str, 
            query: str, tags: list, *args, output_location: str='output', **kwargs):
        self.data = sorted(
                data, 
                key=lambda x: (
                    int(
                        str(x['discount'] or '0').replace('%','').replace('-','')
                    ),
                    parse_float(x['price']), 
                ),
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

        if tags:
            tags = "--".join(list(tags)[:4]).replace(' ','_') + '_'
        else:
            tags = ''

        self.filename = f'{output_location}/{store}_{page_type}_{os}{query}{tags}{timestamp}.csv'


    def write(self):
        with open(self.filename, 'w') as f:
            writer = DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(self.data)
        return self.filename
