from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login, logout

from .forms import CustomUserCreationForm, LoginForm

"""Здесь не использую CBV и базовые представления авторизации django,
             иначе было бы показывать нечего:D"""


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd["username"]
            password = cd["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
        return redirect("/")
    if request.method == "GET":
        form = LoginForm()
        return render(request, "registration/login.html", context={"form": form})
