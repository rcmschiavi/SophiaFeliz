#!/usr/bin/python

import Scraping

#Livros para renovar, colocar os true or false no indice do livro a renovar
livros_renovar=[True, True, False]
Scraping.login()
Scraping.renovacao(livros_renovar)


if len(Scraping.livros)>0:
    print(Scraping.usuario)
    print(Scraping.livros)
    print(Scraping.id_livros)
    print(Scraping.renov_livros)
    print(Scraping.renov_status)

