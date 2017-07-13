#!/usr/bin/python

import Scraping
import json

# Carrega os json para credenciamento para
# evitar que façamos o commit das nossas credenciais
with open( 'credenciais.json' ) as data_file:
    data_params = json.load(data_file)

#Livros para renovar, colocar os true or false no indice do livro a renovar
livros_renovar=[True, True, False]
Scraping.login(data_params['login']['codigo'],data_params['login']['senha'])
Scraping.renovacao(livros_renovar)


if len(Scraping.livros)>0:
    print(Scraping.usuario)
    print(Scraping.livros)
    print(Scraping.id_livros)
    print(Scraping.renov_livros)
    print(Scraping.renov_status)

