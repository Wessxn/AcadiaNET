from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('<str:username>/logout/', views.logout_view, name='logout'),
    path('<str:username>/settings/', views.settings_view, name='settings'),
    path('<str:username>/messages/', views.messages_view, name='messages'),
    path('<str:username>/groupchat/', views.groupchat_view, name='groupchat'),
    path('<str:username>/accs/', views.accs_view, name='accs'),
]