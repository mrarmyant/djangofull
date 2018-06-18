from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    request.session['randomdeal']=get_random_string(length=14)
    if "tries" in request.session:
        request.session['tries'] +=1
    else:
        request.session['tries'] = 1
    return render(request, 'index.html')

def startover(request):
    if 'tries' in request.session:
        request.session.flush()
    return redirect('/')