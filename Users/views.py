from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('flights:home'))
        else:
            return render(request, 'Users/login.html', {
                'error_message': 'ERROR...Invalid Credentials'
            })

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('flights:home'))
    
    else:
        return render(request, 'Users/login.html')

def user_details(request):
    if request.user.is_authenticated:
        return render(request, 'Users/userinfo.html')
    else:
        return render(request, 'Users/login.html', {
            'error_message': 'You must log in first!'
        })

def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('flights:home'))

def register_view(request):
    pass