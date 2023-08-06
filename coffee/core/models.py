from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class Coffee(models.Model):
    """
    title: название кофе
    id: уникальный идентификатор(создается автоматически)
    Описание объекта кофе (поля: id, название)
    """
    title = models.CharField(
        max_length=64,
        verbose_name='Название'

    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кофе'
        verbose_name_plural = 'Кофе'

class Price(models.Model):
    price = models.PositiveIntegerField(
        verbose_name='Цена'
    )

    def __str__(self):
        return str(self.price)

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цена'

class Volume(models.Model):
    title = models.CharField(
        max_length=32,
        verbose_name='Объем'
    )
    price = models.OneToOneField(
        'Price',
        verbose_name='Цена кофе',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объем'
        verbose_name_plural = 'Объем'

class Topping(models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name='Сироп'
    )
    price = models.ForeignKey(
        'Price',
        verbose_name='Цена сиропа',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сироп'
        verbose_name_plural = 'Сироп'

class Profile(AbstractUser) :
    name = models.CharField(
        max_length=64,
        verbose_name='Имя'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    password = models.CharField(
        max_length=24,
        verbose_name='Пароль'
    )

    REQUIRED_FIELDS = ['name', 'password']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'


class Order(models.Model):
    profile = models.ForeignKey(
        'Profile',
        on_delete=models.CASCADE,
        verbose_name='Профиль',
    )
    coffee = models.ForeignKey(
        'Coffee',
        on_delete=models.CASCADE,
        verbose_name='Кофе'
    )
    volume = models.ForeignKey(
        'Volume',
        on_delete=models.CASCADE,
        verbose_name='Объем'
    )
    topping = models.ForeignKey(
        'Topping',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Сироп'
    )
    def get_total_price(self):
        try:
            return self.volume.price.price + self.topping.price.price
        except AttributeError:
            return self.volume.price.price

    get_total_price.short_description = 'Цена заказа'
    def __str__(self):
        return f'{self.profile} {self.coffee}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



