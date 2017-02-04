from django.shortcuts import render
from app.main import get_stat

# Create your views here.

def home(request):

    context = {"bitcoin": get_stat()}
    return render(request,'index.html',context)