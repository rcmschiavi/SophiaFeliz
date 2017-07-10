'''Código para realizar a automação sem utilizar WebDriver'''

# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

#Define como URL o link do frame de login separado para facilitar o parsing da página por ser  em javascript
BASE_URL = 'http://biblioteca.ifsc.edu.br/asp/login.asp?modo_busca=rapida&content=mensagens&iBanner=0&iEscondeMenu=0&iSomenteLegislacao=0&iIdioma=0'
URL = "http://biblioteca.ifsc.edu.br/asp/login.asp?modo_busca=rapida&content=mensagens&iBanner=0&iEscondeMenu=0&iSomenteLegislacao=0&iIdioma=0"
BASE_ACCESS_URL = 'http://biblioteca.ifsc.edu.br/asp/login.asp?modo_busca=rapida&content=mensagens&iBanner=0&iEscondeMenu=0&iSomenteLegislacao=0&iIdioma=0'

# start session
session = requests.Session()
response = session.get(URL, headers={'User-Agent': 'Mozilla/5.0'})

# get frame links
#Caso ocorra algum erro na linha debaixo é necessário fazer um pip install lxml
soup = BeautifulSoup(response.text, 'lxml')
frames = soup.__class__('button_login', 'lxml')

print (frames)
'''
# get header
session.get(header_link, headers={'Referer': URL})

# get document html url
response = session.get(document_link, headers={'Referer': URL})
soup = BeautifulSoup(response.text, 'lxml')

print(soup.text)

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

'''