from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время обновления', auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser, BaseModel):
    username = models.CharField(verbose_name='Логин', max_length=128, blank=False, null=False, unique=True)
    password = models.CharField(verbose_name="Пароль", max_length=128)

    # Избыточные поля базового класса
    last_login = ...
    first_name = ...
    last_name = ...
    date_joined = ...

    USERNAME_FIELD = "username"

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.login
    
    def get_absolute_url(self):
        return reverse("app:edit_user", kwargs={"pk": self.pk})
    

class Item(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='items', verbose_name='Пользователь', blank=True)

    def __str__(self):
        return f'User {self.user.login} item named {self.name}'