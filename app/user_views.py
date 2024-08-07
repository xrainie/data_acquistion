import select
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from app.utils import query, query_or_get_objects_from_cache

from .models import CustomUser

from .forms import CustomUserCreationForm, UserEditForm

"""Здесь не использую CBV и встроенные представления авторизации django,
             иначе было бы показывать нечего:D"""

@login_required
def dashboard_users(request):
    users, items = query()
    context = {
        'users': users,
        'items': items,
        'select': 'users'
    }

    return render(request, 'users.html', context=context)

@login_required
def create_user(request):
    users, items = query_or_get_objects_from_cache()
    message = False
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            message = True
    if request.method == 'GET':
        form = CustomUserCreationForm()
    return render(request, "manage/create.html", {'form': form,
                                               'message': message,
                                               'object': 'User',
                                               'users': users,
                                               'items': items})

@login_required
def delete_user(request, id: int):
    users, items = query_or_get_objects_from_cache()
    if request.method == 'GET':
        return render(request, 'manage/delete_confirm.html', {'users': users, 'items': items, 'select': 'users'})
    if request.method == 'POST':
        user = get_object_or_404(CustomUser, id=id)
        user.delete()
        return redirect(reverse_lazy('app:users'))
    
@login_required
def edit_user_view(request, id: int):
    users, items = query_or_get_objects_from_cache()
    user = get_object_or_404(CustomUser, id=id)
    if request.method == 'POST':
        form = UserEditForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'manage/edit.html', {'form': form,
                                                        'object': 'User',
                                                        'users': users,
                                                        'items': items,
                                                        'select': 'users'})
    if request.method == 'GET':
        form = UserEditForm(instance=user)
        return render(request, 'manage/edit.html', {'form': form,
                                                    'object': 'User',
                                                    'users': users,
                                                    'items': items,
                                                    'select': 'users'})
    return redirect(reverse_lazy('app:users'))