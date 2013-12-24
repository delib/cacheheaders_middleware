cacheheaders_middleware
=======================

Paster-ready WSGI middleware adds cache-controlling headers to the HTTP Response and overrides the Expires header.
This directive flexibly allows caching server to control caching time. 

The package assigns response’s freshness lifetime in the following way:
	
```
    Cache-Control: public, max-age=3600, s-maxage=0
```

The configuration is very simple, a common case being:
```
    [filter:cacheheaders]
    use = egg:cacheheaders_middleware#cache_headers
    max_age=3600
    s_maxage=3600
```

Options
-------

Cacheheaders_middleware enables inserting of the following cache-control headers:

* max_age:

    Maximum age header indicates time (in seconds) for caching the http-response in the browser or caching proxy. 
Cacheheaders_middleware adds “max_age=<value>” to the response and overrides the Expires header.

* s_maxage:
    
    Shared maximum age header indicates time (in seconds) to cache the response in the caching proxy. 
Cacheheaders_middleware adds  “s-maxage=<value>” header to the response and overrides both the Expires header and max_age directive.
