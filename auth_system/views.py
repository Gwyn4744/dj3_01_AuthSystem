from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'auth_system/home.html')

def signup_page(request):
    return render(request, 'auth_system/signup.html')

def login_page(request):
    return render(request, 'auth_system/login.html')

def logout_page(request):
    return render(request, 'auth_system/logout.html')
