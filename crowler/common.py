# coding:utf-8
_author_: "yangrui"

# import urllib
from urllib import request
from urllib.parse import urlparse



def download(url, user_agent='wswp', proxy=None, num_retries=2):
    """Download function with support for proxies"""
    print ('Downloading:', url)
    headers = {'User-agent': user_agent}
    html_request = request.Request(url, headers=headers)
    # print(html_request.get_full_url())
    opener = request.build_opener()

    if proxy:
        proxy_params = {urlparse(url).scheme: proxy}
        opener.add_handler(request.ProxyHandler(proxy_params))
    try:
        html = opener.open(html_request).read()
        # html = request.urlopen(html_request).read()
        html = str(html, encoding='utf-8')
    except request.URLError as e:
        print('downloading error: ', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code <=600:
                return download(url, num_retries=2)
    return html


url = 'http://example.webscraping.com/sitemap.xml'
html = download(url)
print(html)
