from django.shortcuts import render
import random
from django.core.mail import send_mail
from .models import EmailVerification
from django.contrib.auth.models import User

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

def send_verification_code(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'login/verify.html', {'error': 'Email not found.'})

        code = random.randint(100000, 999999)
        EmailVerification.objects.update_or_create(
            user=user,
            defaults={'code': code}
        )

        send_mail(
            'Your Verification Code',
            f'Your verification code is: {code}',
            from_email='acadianet857@gmail.com',
            recipient_list=[email],
            fail_silently=False,
        )
        return render(request, 'login/verify.html', {'message': 'Verification code sent to your email.'})
    return render(request, 'login/verify.html')

