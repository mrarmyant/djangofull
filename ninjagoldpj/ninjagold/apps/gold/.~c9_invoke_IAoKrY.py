from django.shortcuts import render, HttpResponse, redirect


def enterspace(request):
    if farm in request.session:
        request.session["attemptnum"] = 0
    elif cave in:
        sessio
    elif house in:
        request.session['attemptnum'] += 1
    elif casino in:
        
    content = {"randthing" : get_random_string(length=14) }
    return render(request, "generator/index.html", content)

def reset(request):
    if "attemptnum" in request.session:
        request.session.flush()
    return redirect('/random_word/')