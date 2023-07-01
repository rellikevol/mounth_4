from django.db import models
from users.managers import GeekUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class GeekUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="Электронная почта", unique=True)
    is_staff = models.BooleanField(default=False, verbose_name="Персонал")
    is_active = models.BooleanField(default=True, verbose_name="Активный")
    date_joined = models.DateTimeField(default=timezone.now, verbose_name="Дата регистрации")

    USERNAME_FIELD = 'email'
    # обязательные для заполнения поля
    #REQUIRED_FIELDS = []

    objects = GeekUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name ="ГикЮзер"
        verbose_name_plural = "ГикЮзеры"

# Create your models here.
