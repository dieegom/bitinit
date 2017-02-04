from django.shortcuts import render
from app.main import get_stat, get_cambio, get_mkt_share

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
                   "mkt_shr_10d": get_mkt_share("10days")
                   }
        return render(request,'bitinit.html',context)
    except:
        return render(request, 'bitinit.html',"")
