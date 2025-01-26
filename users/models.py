from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    FIRST_ROLE = "user"
    SECOND_ROLE = "admin"

    ROLES_CHOICES = [
        (FIRST_ROLE, "Пользователь"),
        (SECOND_ROLE, "Администратор"),
    ]

    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Укажите ваш Email"
    )
    phone = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name="Номер телефона",
        help_text="Укажите ваш номер телефона",
    )
    first_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Ваше имя",
        help_text="Укажите ваше имя",
    )
    last_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Ваша фамилия",
        help_text="Укажите вашу фамилию",
    )
    role = models.CharField(
        max_length=15, choices=ROLES_CHOICES, default=FIRST_ROLE, verbose_name="Роль"
    )
    image = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите ваш аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = [
            "email",
            "phone",
            "first_name",
            "last_name",
            "role",
        ]

    def __str__(self):
        return self.email
