import logging
from utils import parse_float
from json import load, dump
class GogParser(object):
    def __init__(self, resp: list or dict, *args, **kwargs):
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)
        self.resp = resp

        self.initialize(*args, **kwargs)

    def initialize(self, *args, **kwargs):
        pass

    def parse(self):
        records = []
        try:
            with open('output/gog_tags.json','r') as f:
                tags = load(f)
        except:
            tags = []
        for product in self.resp['products']:
            url_slug = product['slug'].replace('-','_')

            # Their rating is out of 50 on the API, 5 on the site, which is confusing. So 39 is
            #   equivalent to 3.9 out of 5. Calculating this way makes it more intuitive
            try:
                rating_out_of_100 = product['reviewsRating'] * 10 / 500
            except:
                self.log.warning(f"Couldn't calculate rating out of 100 for {product['title']}: {product['reviewsRating']}")
                rating_out_of_100 = None
            for tag in product['tags']:
                if not tag in tags:
                    tags.append(tag)

            if isinstance(product['price'],dict):
                price_obj = product['price']
            else:
                price_obj = {}

            price = price_obj.get('base', '-1') # for coming-soon productStates, price is NoneType
            parsed_price = parse_float(price) if price else None
            discounted_price = price_obj.get('final') 
            discount = price_obj.get('discount') 
            record = {
                'id': product['id'],
                'product_state': product['productState'],
                'name': product['title'],
                'release_dage': product['releaseDate'],
                'product_type': product['productType'],
                'rating_out_of_100': rating_out_of_100,
                'price': price,
                'parsed_price': parsed_price,
                'discounted_price': discounted_price,
                'discount': discount,
                'slug': product['slug'],
                'operating_systems': " | ".join(product['operatingSystems']),
                'raw_rating': product['reviewsRating'],
                'url': f'https://www.gog.com/game/{url_slug}',
            }
            records.append(record)
        with open('output/gog_tags.json','w') as f:
            dump(tags, f, indent=2)
        return records
