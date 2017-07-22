
import subprocess
from subprocess import PIPE
import requests
import time
import json

def tunnel():
    # Inicia o tunnel com certificado para usar no webhook
    subprocess.Popen(r"C:\Users\RodolfoSchiavi\PycharmProjects\SophiaFeliz\chatbot\ngrok http 80",  stderr=PIPE, stdout=PIPE)
    subprocess.Popen(r"python C:\Users\RodolfoSchiavi\PycharmProjects\SophiaFeliz\chatbot\manage.py migrate",stderr=PIPE, stdout=PIPE)
    p = subprocess.Popen(r"python C:\Users\RodolfoSchiavi\PycharmProjects\SophiaFeliz\chatbot\manage.py runserver 0.0.0.0:80", stderr=PIPE, stdout=PIPE)
    print(p.stdout.readline())
    print(p.stdout.readline())
    print(p.stdout.readline())
    print(p.stdout.readline())
    print(p.stdout.readline())
    print(p.stdout.readline())
    print(p.stdout.readline())
    # Sleep para realizar o get sem derrubar o terminal, mas para testes é interessante que o terminal caia pq a porta fica estática
    #time.sleep(5)
    localhost_url = "http://localhost:4040/api/tunnels"
    tunnel_url = requests.get(localhost_url).text
    j = json.loads(tunnel_url)
    tunnel_url = j['tunnels'][1]['public_url']
    print("Use esse url no webhook: ",tunnel_url+"/chatbot")

