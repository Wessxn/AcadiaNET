from django.shortcuts import render

def login_view(request):
    return render(request, 'login/index.html')

def signup_view(request):
    return render(request, 'login/signup.html')

def forget_password_view(request):
    return render(request, 'login/forgetpass.html')