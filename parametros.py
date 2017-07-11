# -*- coding: utf-8 -*-

#Parametros da página de login
url_login = 'http://biblioteca.ifsc.edu.br/asp/login.asp?iIdioma=0&iBanner=0&content=mensagens'
matricula = '666'
senha = '666'
data_login = dict(codigo=matricula,senha=senha, sub_login='sim')
headers_login = {"Host": "biblioteca.ifsc.edu.br",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
           "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
           "Content-Length": "200",
           "Referer": "http://biblioteca.ifsc.edu.br/asp/login.asp?tentativa=1510051880&content=mensagens&veio_de=&codigo_obra=&tipo_obra=&tipo_base=&ano=&volume=&edicao=&biblioteca=&servidor=&iBanner=0&iIdioma=0&type=&dbid=&an="}

#Parametros da página principal
url_main = "http://biblioteca.ifsc.edu.br/sessionData.asp"
url_main_post = "http://biblioteca.ifsc.edu.br/index.asp?modo_busca=rapida"
data_main = dict(modo_busca='rapida')
headers_main = {"Host": "biblioteca.ifsc.edu.br",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
                "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "0",
                "Referer": "http://biblioteca.ifsc.edu.br/spacer.asp"}

#Parametros da página de circulação
url_circ = "http://biblioteca.ifsc.edu.br/index.asp?modo_busca=rapida&content=circulacoes&iFiltroBib=0&iBanner=0&iEscondeMenu=0&iSomenteLegislacao=0&iIdioma=0"
headers_circ = {"Host": "biblioteca.ifsc.edu.br",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
                "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
                "Referer": "http://biblioteca.ifsc.edu.br/index.asp?modo_busca=rapida&content=mensagens&iFiltroBib=0&iBanner=0&iEscondeMenu=0&iSomenteLegislacao=0&iIdioma=0",
                "Upgrade-Insecure-Requests": "1"}