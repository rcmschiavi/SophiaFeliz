# SophiaFeliz
Script de automação para renovação de livros na biblioteca Hercílio Luz.

---
### Instalação:
Para funcionar, requer Python 3 ou superior instalado.

Primeiramente clone o repositório e entre na pasta criada:
`git clone https://github.com/rcmschiavi/SophiaFeliz`
`cd SophiaFeliz`

Então instale as bibliotecas necessárias:
`pip install -r requirements.txt`

### Utilização
`./Main.py`             

---

### To-do:

- Usar a url limpa e passar pra função os parametros como querystring, fazendo com que parametros de sessão e demais fiquem como constantes no código; -> **OK**
- Tornar os parâmetros de login dinâmicos para extrair do DB do projeto final; -> **OK**
- Criar um DB para armazenar as credenciais; -> **OK**
- Criar a parte de escolha dos livros que devem ser renovados; -> **OK**
- Gravar as credenciais no DB depois de verificar a matrícula; -> **OK**
- Criar uma tabela para armazenar informações de renovação -> **OK**;
- Criptografar a senha na inserção e descriptografar na aquisição;
- Criar o script de verificação automática das datas salvas no DB para avisar o usuário;
- Reestruturar o código para separar os procedimentos de chat do script automático;
- Iniciar a implementação do Chatbot.

### Como contribuir:

1. Crie um Fork.
2. Para trabalhar em uma proposta, crie um branch (`git checkout -b proposta_x`)
3. Commit (`git commit -ams "Descrição da proposta"`)
4. Push para o branch da proposta (`git push origin proposta_x`)
5. Abra uma [Pull Request]
6. Vá fazer outra coisa.
