from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'
    choices = (
        ("Пользователь", USER),
        ("Админ", ADMIN),
    )


class User(AbstractBaseUser):
    first_name = models.CharField(verbose_name="Имя", help_text="Введите имя пользователя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", help_text="Введите фамилию пользователя", max_length=50)
    phone = models.CharField(verbose_name="Телефон", help_text="Введите номер телефона", max_length=20)
    email = models.EmailField(verbose_name="Электронная почта", max_length=200,
                              unique=True)  # используется в кач. логина
    role = models.CharField(choices=UserRoles.choices, default='user', max_length=12)
    image = models.ImageField(upload_to='django_media/')
    is_active = models.BooleanField(default=True)

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    # также для работы модели пользователя должен быть переопределен
    # менеджер объектов
    objects = UserManager()

    # для корректной работы нам также необходимо
    # переопределить менеджер модели пользователя

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER
