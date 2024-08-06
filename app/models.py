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