from django.shortcuts import redirect, render
import random
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import EnterCode, LoginForm, PasswordResetForm, ProfileForm
import json
import os

def login_view(request):
    return redirect('/accounts/login/')

def logout_view(request):
    return redirect('/accounts/logout/')

def signup_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login/')
    form = ProfileForm()
    return render(request, 'registration/signup.html', {'form': form})
    
def forget_password_view(request):
    form = PasswordResetForm()
    return render(request, 'registration/forgetpass.html', {'form': form})

def verify_email_view(request):
    return render(request, 'registration/verify.html')

def test_view(request):
    return render(request, 'registration/test.html')

def send_verification_code(request):
    form = EnterCode()  
    code = random.randint(100000, 999999)
    if request.method == 'POST' and 'code' not in request.POST:
        data = json.loads(request.body)
        email = data.get('email')
        send_mail(
                    'Your Verification Code',
                    f'Your verification code is: {code}',
                    from_email = os.getenv('EMAIL_HOST_USER'),
                    recipient_list=[email],
                    fail_silently=False,
                )
        return render(request, 'login/verify.html', {'form': form})
    elif request.method == 'POST' and 'code' in request.POST:
            form = EnterCode(request.POST)
            if form.is_valid():
                entered_code = form.cleaned_data['code']
                if entered_code == code:
                    print("Code verified successfully.")
                else:
                    form.add_error('code', 'Invalid verification code.')
    return render(request, 'registration/verify.html', {'form': form})
