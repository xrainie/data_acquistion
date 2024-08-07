from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import CustomUser, Item

from .forms import CustomUserCreationForm, ItemCreationForm, ItemEditForm, LoginForm, UserEditForm

"""Здесь не использую CBV и встроенные представления авторизации django,
             иначе было бы показывать нечего:D"""


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:               
                login(request, user=user)
                return redirect('/')
            return render(request, "registration/login.html", context={"form": form, "errors": 'Вы ввели неверный логин или пароль.'})
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse_lazy('app:dashboard'))
        form = LoginForm()
    return render(request, "registration/login.html", context={"form": form})

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html')

@login_required
def dashboard(request):
    users = CustomUser.objects.all()
    items = Item.objects.all()

    context = {
        'users': users,
        'items': items
    }

    return render(request, 'dashboard.html', context=context)

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


@login_required
def dashboard_items(request):
    users = CustomUser.objects.all()
    items = Item.objects.all()

    context = {
        'users': users,
        'items': items
    }

    return render(request, 'items.html', context=context)


@login_required
def edit_item_view(request, id: int):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        form = ItemEditForm(instance=item, data=request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'manage/edit.html', {'form': form,
                                                        'object': 'Item'})
    if request.method == 'GET':
        form = ItemEditForm(instance=item)
        return render(request, 'manage/edit.html', {'form': form,
                                                    'object': 'Item'})
    return redirect(reverse_lazy('app:items'))


@login_required
def create_item(request):
    message = False
    if request.method == 'POST':
        form = ItemCreationForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            message = True
    if request.method == 'GET':
        form = ItemCreationForm()
    return render(request, "manage/create.html", {'form': form,
                                               'message': message,
                                               'object': 'Item'})


@login_required
def delete_item(request, id: int):
    if request.method == 'GET':
        return render(request, 'manage/delete_confirm.html')
    if request.method == 'POST':
        item = get_object_or_404(Item, id=id)
        item.delete()
        return redirect(reverse_lazy('app:items'))