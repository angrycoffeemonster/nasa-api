class NasaApiObject(object):
    """docstring for NasaApiObject"""
    def __init__(self, api, **kwargs):
        self._api = api
        for prop in self.Meta.properties:
            val = None
            if prop in kwargs:
                val = kwargs[prop]
            setattr(self, '{0}'.format(prop), val)

    @classmethod
    def from_response(cls, api, response):
        kwargs = {}
        for prop in cls.Meta.properties:
            try:
                kwargs[prop] = response[prop]
            except KeyError:
                pass
        return cls(api, **kwargs)
