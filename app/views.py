from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, LoginForm

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
        # if request.user.is_authenticated:
        #     return redirect('/')
        form = LoginForm()
    return render(request, "registration/login.html", context={"form": form})

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html')