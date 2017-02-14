from django.shortcuts import render
from app.main import get_stat, get_cambio, get_mkt_share, get_chart, get_chart_ord, get_floating_cny, get_floating_blr, get_floating_eur

# Create your views here.

def home(request):

    try:
        context = {"bitcoin": get_stat()}
        return render(request,'index.html',context)
    except:
        return render(request, 'index.html',"")

def wtfisbitcoin(request):

    return render(request, 'wtfisbitcoin.html')

def market(request):

    return render(request, 'market.html')

def bitinit(request):

    try:
        context = {#"bitcoin": get_stat(),
                   # "cambio": get_cambio(),
                   "mkt_shr_7d": get_mkt_share("7days"),
                   "chart_transact_per_sec": get_chart_ord("https://api.blockchain.info/charts/transactions-per-second?timespan=5weeks&rollingAverage=8hours&format=json"),
                   "chart_bitcoin_circ": get_chart_ord("https://api.blockchain.info/charts/total-bitcoins?timespan=5weeks&rollingAverage=8hours&format=json"),
                   # "chart_orph_blocks": get_chart_ord("https://api.blockchain.info/charts/n-orphaned-blocks?timespan=5weeks&rollingAverage=8hours&format=json"),
                   # "chart_hash_rate": get_chart_ord("https://api.blockchain.info/charts/hash-rate?timespan=5weeks&rollingAverage=8hours&format=json"),
                   # "chart_difficult": get_chart_ord("https://api.blockchain.info/charts/difficulty?timespan=5weeks&rollingAverage=8hours&format=json"),
                   # "chart_cost": get_chart_ord("https://api.blockchain.info/charts/cost-per-transaction-percent?timespan=5weeks&rollingAverage=8hours&format=json"),
                   # "chart_wallet": get_chart_ord("https://api.blockchain.info/charts/my-wallet-n-users?timespan=5weeks&rollingAverage=8hours&format=json"),
                   "floating": get_floating_cny(),
                   "floating_btc": get_chart_ord("https://api.blockchain.info/charts/market-price?timespan=5weeks&rollingAverage=8hours&format=json"),
                   "floating_blr": get_floating_blr(),
                   "floating_eur": get_floating_eur(),
                   }
        return render(request,'bitinit.html',context)
    except:
        return render(request, 'bitinit.html',"")
