from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from .managers import UserManager, UserRoles


class User(AbstractBaseUser):
    first_name = models.CharField(verbose_name="Имя", help_text="Введите имя пользователя", max_length=64)
    last_name = models.CharField(verbose_name="Фамилия", help_text="Введите фамилию пользователя", max_length=64)
    phone = models.CharField(verbose_name="Телефон", help_text="Введите номер телефона", max_length=128)
    email = models.EmailField(verbose_name="Электронная почта", max_length=254,
                              unique=True)  # используется в кач. логина
    role = models.CharField(choices=UserRoles.choices, default='user', max_length=12)
    image = models.ImageField(upload_to='django_media/', null=True)
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

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
