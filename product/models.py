from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os


class Category(models.Model):
    name = models.CharField(
        unique=True,
        max_length=100,
        verbose_name='Категория',
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Категория',
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Цена',
    )
    image = models.ImageField(
        upload_to='products/images/',
        blank=True,
        null=True,
        verbose_name='Изображение',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновление'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-updated_at']

    def __str__(self):
        return self.name


@receiver(post_delete, sender=Product)
def product_delete_receiver(sender, instance, **kwargs):
    if instance.image and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)
