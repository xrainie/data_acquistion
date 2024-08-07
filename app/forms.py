from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import fields
from .models import CustomUser, Item

class LoginForm(forms.Form):
    username = forms.CharField(max_length=128, label='Логин')
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=128, label='Логин')
    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2',)


class UserEditForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username', ]


class ItemEditForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name',)


class ItemCreationForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ('name', )