import datetime
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

#ex: https://api.blockchain.info/charts/transactions-per-second?timespan=5weeks&rollingAverage=8hours&format=json
#$timespan Duration of the chart, default is 1 year for most charts, 1 week for mempool charts. (Optional)
#$rollingAverage Duration over which the data should be averaged. (Optional)
#$start Datetime at which to start the chart. (Optional)
#$format Either JSON or CSV, defaults to JSON. (Optional)
#$sampled Boolean set to 'true' or 'false' (default 'true'). If true, limits the number of datapoints returned to ~1.5k for performance reasons. (Optional)
#Please note that values for charts can be represented in scientific notation (14,627,700 is represented as 1.46277E7)
        return a.json()
    except:
        print("sem conexão")

def get_mkt_share(timespan):
    try:
        a = requests.get("https://api.blockchain.info/pools?timespan="+timespan)
        return a.json()
    except:
        print("sem conexão")

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

def get_get():
    a=[]
    try:
        date_init = "2017-01-01"
        date_end = datetime.datetime.today()
        start = datetime.datetime.strptime(date_init, "%Y-%m-%d")

        while start < date_end:
            a.append(requests.get("http://api.fixer.io/"+start.strftime('%Y-%m-%d')+"?symbols=CNY&base=USD").json())
            start = start + datetime.timedelta(days=1)
        return a
    except:
        print(traceback.print_exc(file=sys.stdout))
        return "None"