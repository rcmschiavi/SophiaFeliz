import Scraping
#Livros para renovar, colocar os true or false no indice do livro a renovar
livros_renovar=[True,True,False]
Scraping.login()


if len(Scraping.livros)>0:
    print(Scraping.usuario)
    print(Scraping.livros)
    print(Scraping.id_livros)


Scraping.renovacao(livros_renovar)