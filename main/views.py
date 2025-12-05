from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from .models import ChatRoom, Message
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
User = get_user_model()

# Create your views here.
@login_required
def dashboard_view(request):
    return render(request, 'main/dashboard.html')

@login_required
def settings_view(request, username):
    user = User.objects.get(username=username)
    return render(request, 'main/settings.html', {'user': user})  

@login_required
def logout_view(request):        
    logout(request)
    return redirect('main/login.html')

@login_required
def messages_view(request, username):
    user = User.objects.get(username=username)
    return render(request, 'main/privateMessages.html', {'user': user})

@login_required
def groupchat_view(request, username): 
    user  = User.objects.get(username=username)
    return render(request, 'main/gc.html', {'user':user})

@login_required
def accs_view(request, username):
    user = User.objects.get(username=username)
    return render(request, 'main/acss.html', {'user': user})