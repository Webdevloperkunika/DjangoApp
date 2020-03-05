from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
def loginpage(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password =  request.POST['password']
        post = User.objects.filter(username=username)
        if post:
            username = request.POST['username']
            request.session['username'] = username
            return redirect("profile")
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})
def profile(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = User.objects.filter(username=posts) 
        return render(request, 'profile.html', {"query":query})
    else:
        return render(request, 'login.html', {})

def logout(request):
    try:
        del request.session['username']
    except:
     pass
    return render(request, 'app_foldername/login.html', {})

def dashboard(request):
    # Dashboard Page
    return render(request, "dashboard.html")
def blank(request):
    # blank redirect Page
    return redirect('/admin')
def login(request):
    # blank redirect Page
    return render(request, "login.html")



