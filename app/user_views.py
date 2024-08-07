from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import CustomUser, Item

from .forms import CustomUserCreationForm, UserEditForm


@login_required
def dashboard_users(request):
    users = CustomUser.objects.all()
    items = Item.objects.all()

    context = {
        'users': users,
        'items': items
    }

    return render(request, 'users.html', context=context)

@login_required
def create_user(request):
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
                                               'object': 'User'})

@login_required
def delete_user(request, id: int):
    if request.method == 'GET':
        return render(request, 'manage/delete_confirm.html')
    if request.method == 'POST':
        user = get_object_or_404(CustomUser, id=id)
        user.delete()
        return redirect(reverse_lazy('app:users'))
    
@login_required
def edit_user_view(request, id: int):
    user = get_object_or_404(CustomUser, id=id)
    if request.method == 'POST':
        form = UserEditForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'manage/edit.html', {'form': form,
                                                        'object': 'User'})
    if request.method == 'GET':
        form = UserEditForm(instance=user)
        return render(request, 'manage/edit.html', {'form': form,
                                                    'object': 'User'})
    return redirect(reverse_lazy('app:users'))