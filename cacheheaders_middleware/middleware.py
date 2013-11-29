from paste.httpheaders import CACHE_CONTROL


class CustomHeadersHandler(object):
    """
    """
    def __init__(self, application, max_age, s_maxage):
        self.application = application
        self.max_age = max_age
        self.s_maxage = s_maxage

    def __call__(self, environ, start_response):
        response = self.application(environ, start_response)
        if 'no-cache' not in CACHE_CONTROL(environ):
            CACHE_CONTROL.apply(start_response.__self__.wsgi_curr_headers[1],
                                public=True,
                                max_age=self.max_age,
                                s_maxage=self.s_maxage)
        return response


def make_wsgi_middleware(app, global_conf, max_age, s_maxage, **kw):
    """
    Config looks like this::

      [filter:cacheheaders]
      use = egg:cacheheaders_middleware#cache_headers
      max_age=3600
      s_maxage=36000
      
    """
    return CustomHeadersHandler(app, int(max_age), int(s_maxage))
