import Scraping
#Livros para renovar, colocar os true or false no indice do livro a renovar
livros_renovar=[True,False,False]
Scraping.login()


if len(Scraping.livros)>0:
    print(Scraping.usuario)
    print(Scraping.livros)

#função renovação está com bugs na parte de enviar o código dos livros a serem renovados e na vizualização da resposta da page
#deve ser feita o encode do string para ser aceito no get
Scraping.renovacao(livros_renovar)