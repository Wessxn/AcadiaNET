from django.shortcuts import render

def login_view(request):
    return render(request, 'login/login.html')

def signup_view(request):
    return render(request, 'login/signup.html')