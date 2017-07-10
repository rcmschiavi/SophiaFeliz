import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import requests


BASE_URL = 'http://www.un.org/en/ga/search/'
URL = "http://www.un.org/en/ga/search/view_doc.asp?symbol=A/RES/68/278"
BASE_ACCESS_URL = 'http://daccess-ods.un.org'

# start session
session = requests.Session()
response = session.get(URL, headers={'User-Agent': 'Mozilla/5.0'})

# get frame links
soup = BeautifulSoup(response.text, 'lxml')
frames = soup.find_all('frame')
header_link, document_link = [urljoin(BASE_URL, frame.get('src')) for frame in frames]

# get header
session.get(header_link, headers={'Referer': URL})

# get document html url
response = session.get(document_link, headers={'Referer': URL})
soup = BeautifulSoup(response.text, 'lxml')

content = soup.find('meta', content=re.compile('URL='))['content']
document_html_link = re.search('URL=(.*)', content).group(1)
document_html_link = urljoin(BASE_ACCESS_URL, document_html_link)

# follow html link and get the pdf link
response = session.get(document_html_link)
soup = BeautifulSoup(response.text, 'lxml')

# get the real document link
content = soup.find('meta', content=re.compile('URL='))['content']
document_link = re.search('URL=(.*)', content).group(1)
document_link = urljoin(BASE_ACCESS_URL, document_link)
print (document_link)

# follow the frame link with login and password first - would set the important cookie
auth_link = soup.find('frame', {'name': 'footer'})['src']
session.get(auth_link)

# download file
with open('document.pdf', 'wb') as handle:
    response = session.get(document_link, stream=True)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)