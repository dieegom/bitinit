from django.shortcuts import render
from app.main import get_stat, get_cambio, get_mkt_share, get_chart

# Create your views here.

def home(request):

    try:
        context = {"bitcoin": get_stat()}
        return render(request,'index.html',context)
    except:
        return render(request, 'index.html',"")

def bitinit(request):

    try:
        context = {"bitcoin": get_stat(),
                   "cambio": get_cambio(),
                   "mkt_shr_1d": get_mkt_share("1days"),
                   "mkt_shr_5d": get_mkt_share("5days"),
                   "mkt_shr_10d": get_mkt_share("10days"),
                   "chart_transact_per_sec": get_chart("https://api.blockchain.info/charts/transactions-per-second?timespan=5weeks&rollingAverage=8hours&format=json"),
                   "chart_bitcoin_circ": get_chart("https://api.blockchain.info/charts/total-bitcoins?timespan=5weeks&rollingAverage=8hours&format=json"),
                   "chart_market_price": get_chart("https://api.blockchain.info/charts/market-price?timespan=5weeks&rollingAverage=8hours&format=json"),
                   "chart_orph_blocks": get_chart("https://api.blockchain.info/charts/n-orphaned-blocks?timespan=5weeks&rollingAverage=8hours&format=json"),
                   "chart_hash_rate": get_chart("https://api.blockchain.info/charts/hash-rate?timespan=5weeks&rollingAverage=8hours&format=json"),
                   "chart_difficult": get_chart("https://api.blockchain.info/charts/difficulty?timespan=5weeks&rollingAverage=8hours&format=json"),
                   "chart_cost": get_chart("https://api.blockchain.info/charts/cost-per-transaction-percent?timespan=5weeks&rollingAverage=8hours&format=json"),
                   "chart_wallet": get_chart("https://api.blockchain.info/charts/my-wallet-n-users?timespan=5weeks&rollingAverage=8hours&format=json"),
                   }
        return render(request,'bitinit.html',context)
    except:
        return render(request, 'bitinit.html',"")
