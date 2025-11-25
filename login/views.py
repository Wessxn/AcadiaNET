from django.shortcuts import redirect, render
import random
from django.core.mail import send_mail
from .models import EmailVerification
from django.contrib.auth.models import User, auth 
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
import json

def login_view(request):
    return render(request, 'login/index.html')

def signup_view(request):
    return render(request, 'login/signup.html')

def forget_password_view(request):
    return render(request, 'login/forgetpass.html')

def verify_email_view(request):
    return render(request, 'login/verify.html')

def reset_password_view(request):
    return render(request, 'login/reset_password.html')

def home_view(request):
    return render(request, 'login/home.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("home") 
        else:
            return render(request, "login/index.html", {"error": "Invalid credentials"})

    return render(request, "login/index.html") 

# def register_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         if User.objects.filter(username=username).exists():
#             return render(request, 'login/signup.html', {'error': 'Username already exists.'})

#         if User.objects.filter(email=email).exists():
#             return render(request, 'login/signup.html', {'error': 'Email already registered.'})

#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.save()
#         return redirect('home')
#     return render(request, 'login/signup.html')



def verify(request):
    if request.method == 'POST':
        print("POST request received for sending verification code.")
        data = json.loads(request.body)
        email = data.get('email')
        print("Email:", email)
        verification_code = str(random.randint(100000, 999999))
        print("Generated Verification Code:", verification_code)
        send_mail(
        subject='AcadiaNET Test Email',
        message='This is your verification code: ' + verification_code,
        from_email='acadianet857@gmail.com',
        recipient_list=[email], 
    )
    return render(request, 'login/verify.html')

def confirm_code(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        entered_code =  data.get('code')
        print("Entered Code:", entered_code)

# def reset_password(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         new_password = request.POST.get('new_password')

#         try:
#             user = User.objects.get(email=email)
#             user.set_password(new_password)
#             user.save()
#             return render(request, 'login/login.html', {'message': 'Password reset successful. Please log in.'})
#         except User.DoesNotExist:
#             return render(request, 'login/reset_password.html', {'error': 'Email not found.'})

#     return render(request, 'login/reset_password.html')

def send_test_email(request):
    send_mail(
        subject='AcadiaNET Test Email',
        message='This is a test email sent from your Django app.',
        from_email='acadianet857@gmail.com',
        recipient_list=['parkermarcus282@gmail.com'], 
    )
    return HttpResponse("Email sent successfully!")
