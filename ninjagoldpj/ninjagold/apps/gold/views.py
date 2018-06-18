from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if request.path == "/farm":
        if "gold" in request.session:
            request.session['gold']+=random.randint(10,21)
        else:
            request.session['gold']=random.randint(10,21)
    elif request.path == "/cave":
        if "gold" in request.session:
            request.session['gold']+=random.randint(5,11)
        else:
            request.session['gold']=random.randint(5,11)
    elif request.path == "/house":
        if "gold" in request.session:
            request.session['gold']+=random.randint(2,6)
        else:
            request.session['gold']=random.randint(2,6)
    elif request.path == "/casino":
        if "gold" in request.session:
            request.session['gold']+=random.randint(-50,51)
        else:
            request.session['gold']=random.randint(-50,51)
    return render(request, "gold/index.html")