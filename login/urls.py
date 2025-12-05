from django.urls import include, path
from . import views
import main.urls  as main_urls

urlpatterns = [
    path('', views.login_view, name='test'),
    path('', include(main_urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup_view, name='signup'),
    path('forgetpass/', views.forget_password_view, name='forgetpass'),
]
