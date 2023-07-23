from django.db import models



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
        return self.price

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
        on_delete=models.CASCADE()
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сироп'
        verbose_name_plural = 'Сироп'

class Profile(models.Model):
    pass

class Order(models.Model):
    pass
