from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if "attemptnum" in request.session:
        request.session["attemptnum"] = 0
        
    else:
        request.session['attemptnum'] += 1
    content = {"randthing" : get_random_string(length=14) }
    return render(request, "generator/index.html", content)

def reset(request):
    if "attemptnum" in request.session:
        request.session.flush()
    return redirect('/random_word/')