from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('', views.dashboard, name='dashboard'),
    path('users/', views.dashboard_users, name='users'),
    path('users/add/', views.create_user, name='create_user'),
    path('users/delete/<int:id>/', views.delete_user, name='delete_user'),
    path('users/edit/<int:id>', views.edit_user_view, name='edit_user'),

    path('items/', views.dashboard_items, name='items'),
    path('items/add/', views.create_item, name='create_item'),
    path('items/delete/<int:id>/', views.delete_item, name='delete_item'),
    path('items/edit/<int:id>', views.edit_item_view, name='edit_item'),
]
