from lxml.html import fromstring
import logging
class HTMLParser(object):
    def __init__(self, raw_html: str or bytes, *args, **kwargs):
        self.etree = fromstring(raw_html)
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)

        self.initialize(*args, **kwargs)

    def initialize(self, *args, **kwargs):
        pass

    def parse(self):
        pass
