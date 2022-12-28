from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


#@login_required
def Index(request):
    return render(request, 'index.html')

def Home(request):
    return render(request, 'home.html')

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        return redirect('index')

    return render(request, 'register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        return redirect('index')

    return render(request, 'login.html')