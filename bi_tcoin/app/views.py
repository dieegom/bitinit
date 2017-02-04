from django.shortcuts import render
from app.main import get_stat, get_cambio

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
                   }
        return render(request,'bitinit.html',context)
    except:
        return render(request, 'bitinit.html',"")
