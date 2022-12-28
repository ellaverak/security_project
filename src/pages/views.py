from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pages.controller as controller
#from pages.db import cursor


#@login_required
def Index(request):
    return render(request, 'index.html')

def Home(request):
    return render(request, 'home.html')

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if controller.register(username, password):
            return render(request, 'index.html')

    return render(request, 'register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        return render(request, 'index.html')

    return render(request, 'login.html')