import requests

#funciona se for dentro do venv35 na pasta (~/Documents/Bitenv) digitando: source vir35/bin/activate
#depois eh soh entrar na pasta ~/PycharmProjects/BItcoin e digitar: python main.py

def get_stat():
    try:
        a = requests.get("https://api.blockchain.info/stats")
        return a.json()
    except:
        print("sem conexão")

def get_cambio():
    try:
        a = requests.get("https://blockchain.info/ticker")
        return a.json()
    except:
        print("sem conexão")
