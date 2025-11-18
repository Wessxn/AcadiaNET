from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('forgetpass/', views.forget_password_view, name='forgetpass'),
]
