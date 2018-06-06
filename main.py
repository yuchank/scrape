from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        v = bs.body.h1
    except AttributeError:
        return None
    return v


title = get_title('http://www.pythonscraping.com/pages/page1.html')
if title is None:
    print('Title could not be found')
else:
    print(title)
