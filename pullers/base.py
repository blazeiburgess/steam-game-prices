from requests import Request, Session
class BasePuller(object):
    base_headers = {}
    def __init__(self, *args, session_args=[], session_kwargs={}, **kwargs):
        self.sess = Session(*session_args, **session_kwargs)

        self.initialize(*args, **kwargs)

    def initialize(self, *args, **kwargs):
        pass

    def _make_request(self, method, url, *args, headers={}, **kwargs):
        headers = {**headers, **self.base_headers}
        req = Request(method, url, *args, headers=headers, **kwargs)
        prep = req.prepare()
        return self.sess.send(prep)

    def _get(self, url, *args, **kwargs):
        return self._make_request(
                'GET', url,
                *args, **kwargs
            )

    def _post(self, url, *args, **kwargs):
        return self._make_request(
                'POST', url,
                *args, **kwargs
            )
