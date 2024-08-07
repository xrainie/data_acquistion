from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser

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