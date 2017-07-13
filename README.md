# SophiaFeliz
Script de automação para renovação de livros na biblioteca Hercílio Luz.

---
### Configurações

Para modificar as **credenciais** dentro do credenciais.json, é recomendado que
antes seja executado `git update-index --skip-worktree credenciais.json`, para que os credenciais não corram risco de entrar para o git.

### To-do

- Usar a url limpa e passar pra função os parametros como querystring, fazendo com que parametros de sessão e demais fiquem como constantes no código -> **OK**
- Tornar os parâmetros de login dinâmicos para extrair do DB do projeto final -> **OK**;
- Implementar um DB para armazenar as credenciais.
