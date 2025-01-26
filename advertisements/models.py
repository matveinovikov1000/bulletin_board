from django.db import models
from users.models import User


class Announcement(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Название товара",
        help_text="Укажите название товара",
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена товара", help_text="Укажите цену товара"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание товара",
        help_text="Укажите описание товара",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор объявления",
        help_text="Укажите автора объявления",
        related_name="announcements",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Дата и время создания объявления"
    )

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = [
            "title",
            "price",
            "description",
            "author",
            "created_at",
        ]

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(
        verbose_name="Отзыв", help_text="Укажите текст отзыва на товар"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Автор отзыва",
        help_text="Укажите автора отзыва",
        related_name="reviews",
    )
    ad = models.ForeignKey(
        Announcement,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Объявление, под которым указан отзыв",
        help_text="Укажите объявление, под которым указан отзыв",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Дата и время создания отзыва"
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = [
            "text",
            "author",
            "ad",
            "created_at",
        ]

    def __str__(self):
        return self.text
