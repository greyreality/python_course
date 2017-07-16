from urllib.parse import urlparse, parse_qs

url="http://test.com?key1=1&key2=2&key3=3"
url_matcher="http://test.com?key3=3&key2=2&key1=1"

def test_url_scheme_and_netloc():
    # URL parse
    url_parse = urlparse(url)
    url_matcher_parse = urlparse(url_matcher)
    # get URLs without query
    url_with_no_query = url_parse._replace(query=None).geturl()
    url_matcher_with_no_query = url_matcher_parse._replace(query=None).geturl()
    # compare URLs without query
    assert (url_with_no_query == url_matcher_with_no_query
            ), 'URL %s has wrong scheme or netloc' % url

def test_url_query():
    # URL parse
    url_parse = urlparse(url)
    url_matcher_parse = urlparse(url_matcher)
    # get queries from URLS
    url_query = parse_qs(url_parse.query)
    url_matcher_query = parse_qs(url_matcher_parse.query)
    # compare queries from URLS
    assert (url_query == url_matcher_query),'URL %s has wrong query' % url