from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.login_view, name='test'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup_view, name='signup'),
    path('forgetpass/', views.forget_password_view, name='forgetpass'),
    path('verify/', views.send_verification_code, name='verify'),
    path('test/', views.test_view, name='test'),
]
