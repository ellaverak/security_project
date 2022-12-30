from django.shortcuts import render, redirect
import pages.controller as controller


def Index(request):
    return render(request, 'index.html')

def Home(request):
    #try:
    #    user_id = controller.return_user_id()
    #    if user_id == None:
    #        raise
    #except:
    #    return redirect('/')
    #BROKEN ACCESS CONTROL
    references = controller.get_references()
    return render(request, 'home.html', {'references': references})

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if controller.register(username, password):
            return redirect('/home')

    return render(request, 'register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if controller.login(username, password):
            return redirect('/home')

    return render(request, 'login.html')

def Logout(request):
    controller.logout()

    return redirect('/')

def Save(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        name = request.POST.get('name')
        publisher = request.POST.get('publisher')
        year = request.POST.get('year')

        controller.save(author, name, publisher, year)

    return redirect('/home')
