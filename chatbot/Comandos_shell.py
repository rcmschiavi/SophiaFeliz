
import subprocess
from subprocess import PIPE
import requests
import time
import json
import os
from sys import platform

def tunnel():
    # Pega os caminhos dinamicamente
    sophia_ROOT_DIR = os.getcwd()
    chatbot_DIR = os.path.join(sophia_ROOT_DIR, "chatbot")
    manage_PY = os.path.join(sophia_ROOT_DIR, "manage.py")
    ngrok_BIN = os.path.join(chatbot_DIR, "ngrok")

    # Inicia o tunnel com certificado para usar no webhook
    subprocess.Popen([ngrok_BIN, "http", "80"],  stderr=PIPE, stdout=PIPE)
    subprocess.Popen(["python", manage_PY, "migrate"], stderr=PIPE, stdout=PIPE)

    # No Linux é necessário permissões para subir na porta 80. Rodar via SUDO
    # talvez não seja a idéia mais segura.
    if platform.lower() == "linux" or platform.lower() == "linux2":
        p = subprocess.Popen(["sudo", "python", manage_PY, "runserver", "localhost:80"], stderr=PIPE, stdout=PIPE)
    elif platform.lower() == "darwin": # OS X
        # Não sei se roda.
        p = subprocess.Popen(["sudo", "python", manage_PY, "runserver", "localhost:80"], stderr=PIPE, stdout=PIPE)
    elif platform.lower().startswith("win"):
        p = subprocess.Popen(["python", manage_PY, "runserver", "localhost:80"], stderr=PIPE, stdout=PIPE)

    # isso está fazendo com que o programa trave:
    #print(p.stdout.readline())
    #print(p.stdout.readline())
    #print(p.stdout.readline())
    #print(p.stdout.readline())
    #print(p.stdout.readline())
    #print(p.stdout.readline())
    #print(p.stdout.readline())
    # Sleep para realizar o get sem derrubar o terminal, mas para testes é interessante que o terminal caia pq a porta fica estática
    #time.sleep(5)
    localhost_url = "http://localhost:4040/api/tunnels"
    tunnel_url = requests.get(localhost_url).text
    j = json.loads(tunnel_url)
    tunnel_url = j['tunnels'][1]['public_url']
    print("Use esse url no webhook: ",tunnel_url+"/chatbot")

