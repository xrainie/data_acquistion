from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время обновления', auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractBaseUser, BaseModel):
    login = models.CharField(verbose_name='Логин', max_length=30, blank=False, null=False, unique=True)
    password = models.CharField(verbose_name="Пароль", max_length=128)

    # Избыточное поле
    last_login = ...

    USERNAME_FIELD = "login"

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.login
    

class Item(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='items', verbose_name='Пользователь')

    def __str__(self):
        return f'User {self.user.login} item named {self.name}'