from csv import DictWriter
class CSVWriter(object):
    def __init__(self, data: dict, fieldnames: list, store: str, page_type: str, timestamp: int, *args, output_location: str='output', **kwargs):
        self.data = data
        self.fieldnames = fieldnames

        #TODO: make filename structure an argument
        self.filename = f'{output_location}/{store}_{page_type}_{timestamp}.csv'


    def write(self):
        with open(self.filename, 'w') as f:
            writer = DictWrtier(fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(self.data)
