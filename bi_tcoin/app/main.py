import datetime
import operator
import traceback

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

def get_chart(chart):
    try:
        a = requests.get(chart)
        return a.json()
    except:
        print("sem conexão")

def get_chart_ord(chart):
    try:
        a = requests.get(chart)
        b = a.json()
        c = []
        for item in b['values']:
            c.append([item['x'], item['y']])
        return c
    except:
        print("sem conexão")

def get_mkt_share(timespan):
    try:
        a = requests.get("https://api.blockchain.info/pools?timespan="+timespan)
        b = a.json()
        s = [[k,v] for v,k in sorted(
            [[v,k] for k,v in b.items()],reverse=True
            )
            ]
        return s
    except:
        print("sem conexão")

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

def get_cambio(moeda,weeks):
    a = []
    try:
        date_end = datetime.datetime.today()
        date_init = date_end - datetime.timedelta(days=7*weeks)
        start = date_init
        while start < date_end:
            a.append(requests.get("http://api.fixer.io/"+start.strftime('%Y-%m-%d')+"?symbols="+moeda+"&base=USD").json())
            start = start + datetime.timedelta(days=1)
        c = []
        for item in a:
            c.append([item['date'],item['rates'][moeda]])
        return c

    except:
        print(traceback.print_exc(file=sys.stdout))
        return "None"

def get_floating_cny():

    try:
        cny = get_cambio("CNY",1)
        bitcoin = get_chart_ord("https://api.blockchain.info/charts/market-price?timespan=1weeks&rollingAverage=1hours&format=json")

        floater = [['Dias', 'Bitcoins em USD', 'CNY em USD'],]

        for cont in range(0, len(bitcoin)):
            floater.append([cny[cont][0], bitcoin[cont][1], cny[cont][1]*1000.0])

        return floater

    except:
        print("f#$%#@ck")

def get_floating_blr():

    try:
        brl = get_cambio("BRL",1)
        bitcoin = get_chart_ord("https://api.blockchain.info/charts/market-price?timespan=1weeks&rollingAverage=1hours&format=json")

        floater = [['Dias', 'Bitcoins em USD', 'BRL em USD x 10^-2'],]

        for cont in range(0, len(bitcoin)):
            floater.append([brl[cont][0], bitcoin[cont][1], brl[cont][1]*100])

        return floater

    except:
        print("f#$%#@ck")

def get_floating_eur():

    try:
        eur = get_cambio("EUR",1)
        bitcoin = get_chart_ord("https://api.blockchain.info/charts/market-price?timespan=1weeks&rollingAverage=1hours&format=json")

        floater = [['Dias', 'Bitcoins em USD', 'EUR em USD x 10^-2'],]

        for cont in range(0, len(bitcoin)):
            floater.append([eur[cont][0], bitcoin[cont][1], eur[cont][1]*100])

        return floater

    except:
        print("f#$%#@ck")

