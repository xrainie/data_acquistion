from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('', views.dashboard, name='dashboard'),
    path('users/', views.dashboard_users, name='users'),
]
