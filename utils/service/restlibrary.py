from requests.sessions import Session


class RestLib(Session):
    """
        Library for REST API Calls
    """

    def get(self, url, **kwargs):
        """Sends a GET request. Returns :class:`Response` object.
        Args:
        :param url: URL for the new :class:`Request` object.
        :param kwargs: Optional arguments that ``request`` takes.
        """

        kwargs.setdefault('timeout', 60)
        kwargs.setdefault('allow_redirects', True)
        return self.request('GET', url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        """Sends a POST request. Returns :class:`Response` object.
        Args:
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the :class:`Request`.
        :param kwargs: Optional arguments that ``request`` takes.
        """

        kwargs.setdefault('timeout', 60)
        return self.request('POST', url, data=data, json=json, **kwargs)

    def put(self, url, data=None, **kwargs):
        """Sends a PUT request. Returns :class:`Response` object.
        Args:
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
        :param kwargs: Optional arguments that ``request`` takes.
        """

        kwargs.setdefault('timeout', 60)
        return self.request('PUT', url, data=data, **kwargs)