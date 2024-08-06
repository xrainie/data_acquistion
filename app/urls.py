from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # path('/', ), 
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
