from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import CustomUser, Item

from .forms import CustomUserCreationForm, LoginForm, UserEditForm

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
    return render(request, "createuser.html", {'form': form,
                                               'message': message})

@login_required
def delete_user(request, id: int):
    user = get_object_or_404(CustomUser, id=id)
    if request.method == 'GET':
        return render(request, 'delete_confirm.html', {'user': user})
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
            return render(request, 'edituser.html', {'form': form})
    if request.method == 'GET':
        form = UserEditForm(instance=user)
        return render(request, 'edituser.html', {'form': form})
    return redirect(reverse_lazy('app:users'))