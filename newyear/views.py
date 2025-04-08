from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.

def index(request):

    now=datetime.datetime.now()
    return render(request,"newyear/index.html",{
        "newyear":now.month==1 and now.day==1,
        "next_newyear":datetime.datetime(now.year+1,1,1),
        "message":"Happy New Year!" if now.month==1 and now.day==1 else "Not Happy New Year",
        "now":now
    })
