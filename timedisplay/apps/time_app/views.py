from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from dateutil.tz import tzutc, tzlocal

def index():
    return redirect('/time_app/')

def time(request):
    now=datetime.now()
    siteCrap={
        "time": now
    }
    return render(request,'time_app/index.html', siteCrap)