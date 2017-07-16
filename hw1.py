from urllib.parse import urlparse, parse_qs

url = "http://test.com?key1=1&key2=2&key3=3"
url_matcher = "http://test.com?key3=3&key2=2&key1=1"

def checkSchemeAndNetloc(url,url_matcher):
    # URL parse
    url_parse_result = urlparse(url)
    url_matcher_parse_result = urlparse(url_matcher)
    # get URLs without query
    url_with_no_query = url_parse_result._replace(query=None).geturl()
    url_matcher_with_no_query = url_matcher_parse_result._replace(query=None).geturl()
    #compare URLs without query
    assert (url_with_no_query == url_matcher_with_no_query),'URL %s has wrong scheme or netloc' % url
    print(url_with_no_query,'\t',url_matcher_with_no_query)

def checkQuery(url,url_matcher):
    # URL parse
    url_parse_result = urlparse(url)
    url_matcher_parse_result = urlparse(url_matcher)
    # get query from URLS
    url_query = parse_qs(url_parse_result.query)
    url_matcher_query = parse_qs(url_matcher_parse_result.query)
    #compare queries
    assert (url_query == url_matcher_query),'URL %s has wrong query' % url
    print(url_query,'\t', url_matcher_query)

checkSchemeAndNetloc(url,url_matcher)
checkQuery(url,url_matcher)