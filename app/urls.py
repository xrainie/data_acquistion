from django.urls import path
from . import views
from . import item_views
from . import user_views

app_name = 'app'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),
    
    path('users/', user_views.dashboard_users, name='users'),
    path('users/add/', user_views.create_user, name='create_user'),
    path('users/delete/<int:id>/', user_views.delete_user, name='delete_user'),
    path('users/edit/<int:id>', user_views.edit_user_view, name='edit_user'),

    path('items/', item_views.dashboard_items, name='items'),
    path('items/add/', item_views.create_item, name='create_item'),
    path('items/delete/<int:id>/', item_views.delete_item, name='delete_item'),
    path('items/edit/<int:id>', item_views.edit_item_view, name='edit_item'),
]
