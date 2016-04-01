import pycurl
from BeautifulSoup import BeautifulSoup
from StringIO import StringIO


def get_html_search_root(link):
    buf = StringIO()
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, link)
    curl.setopt(pycurl.WRITEDATA, buf)
    curl.perform()
    curl.close()
    html = buf.getvalue()
    soup = BeautifulSoup(html)
    return soup.html.body

if __name__ == '__main__':
    print get_html_search_root('http://finance.i.ua')