from lxml.html import fromstring
class HTMLParser(object):
    def __init__(self, raw_html: str or bytes, *args, **kwargs):
        self.etree = fromstring(raw_html)

        self.initialize(*args, **kwargs)

    def initialize(self, *args, **kwargs):
        pass

    def parse(self):
        pass
