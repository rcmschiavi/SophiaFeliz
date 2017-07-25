# SophiaFeliz
Script (independente) para renovação automatizada de livros/circulações para bibliotecas que usam o sistema [SophiA](http://www.portalsophia.com.br).

**EM DESENVOLVIMENTO. AINDA NÃO FUNCIONAL**

---

## Servidor (Python)

### Instalação:
Para funcionar, requer Python 3 ou superior instalado.

Primeiramente clone o repositório e entre na pasta criada:
`git clone https://github.com/rcmschiavi/SophiaFeliz && cd SophiaFeliz`

Então instale as bibliotecas necessárias:
`pip install -r requirements.txt`

### Configurações e Utilização
Algumas configurações são necessárias dependendo do modo de teste desejado.
Para testar online no Facebook, é necessário criar uma conta no [Facebook Developers](developers.facebook.com), um app e utilizar o produto **Messenger**, além de uma página.

No arquivo `chatbot/settings.py`:
-`<myfacebookdevelopersappsecret>` deve ser substituído pelo **App Secret** do app. 
-`<myfacebookpagetoken>` deve ser substituído pelo token do Messenger linkado à
página criada.

O servidor deve ser iniciado:
`./Main.py`             

No [Facebook Developers](developers.facebook.com) deve-se colar o link fornecido
pelo servidor (main.py) e selecionar os eventos `messages, messaging_postbacks, messaging_optins, message_deliveries`.

---

### To-do:

- Usar a url limpa e passar pra função os parametros como querystring, fazendo com que parametros de sessão e demais fiquem como constantes no código; -> **OK**
- Tornar os parâmetros de login dinâmicos para extrair do DB do projeto final; -> **OK**
- Criar um DB para armazenar as credenciais; -> **OK**
- Criar a parte de escolha dos livros que devem ser renovados; -> **OK**
- Gravar as credenciais no DB depois de verificar a matrícula; -> **OK**
- Criar uma tabela para armazenar informações de renovação; -> **OK**
- Criar o script de verificação automática das datas salvas no DB para avisar o usuário -> **OK**
- Reestruturar o código para separar os procedimentos de chat do script automático; -> **Em processo...**
- Iniciar a implementação do Chatbot; -> **OK**
- Conectar o chatbot no restante do script -> **Em processo...*
- Criptografar a senha na inserção e descriptografar na aquisição;
- Organizar lista de frases recebidas e de frases enviadas;

### Como contribuir:

1. Crie um Fork.
2. Para trabalhar em uma proposta, crie um branch (`git checkout -b proposta_x`)
3. Commit (`git commit -m "Descrição da proposta"`)
4. Push para o branch da proposta (`git push origin proposta_x`)
5. Abra uma [Pull Request]
6. Vá fazer outra coisa.
