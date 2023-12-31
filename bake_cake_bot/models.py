import uuid

from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Users(UUIDMixin, TimeStampedMixin):
    telegram_id = models.IntegerField(unique=True, default=False)
    username = models.CharField(max_length=64, null=True, verbose_name='UserName')
    name = models.CharField(max_length=256, null=True, verbose_name='Имя')
    phone = PhoneNumberField(verbose_name='Номер телефона', blank=True)
    registration = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.username:
            return f'@{self.username}'
        else:
            return f'{self.telegram_id}'

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


class Order(models.Model):
    number = models.AutoField(verbose_name='Номер заказа', primary_key=True, unique=True)
    username = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    price = models.FloatField(verbose_name='Цена', default=0.0)
    init_date = models.DateTimeField(verbose_name='Дата создания заказа',default=timezone.now())
    delivery_date = models.DateTimeField(verbose_name='Дата и время доставки', default=None)
    address = models.TextField(verbose_name='Адрес доставки', max_length=500)

    def __str__(self):
        return f'Заказ номер {self.number}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Layer(models.Model):
    name = models.CharField(
        verbose_name='Слой',
        max_length=50
    )
    price = models.FloatField(
        verbose_name='Цена',
        default=0.0
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Слой'
        verbose_name_plural = 'Слои'


class Shape(models.Model):
    name = models.CharField(
        verbose_name='Форма',
        max_length=50
    )
    price = models.FloatField(
        verbose_name='Цена',
        default=0.0
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'


class Topping(models.Model):
    name = models.CharField(
        verbose_name='Топпинг',
        max_length=50
    )
    price = models.FloatField(
        verbose_name='Цена',
        default=0.0
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Топинг'
        verbose_name_plural = 'Топинги'


class Berries(models.Model):
    name = models.CharField(
        verbose_name='Ягоды',
        max_length=50
    )
    price = models.FloatField(
        verbose_name='Цена',
        default=0.0
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ягода'
        verbose_name_plural = 'Ягоды'


class Decor(models.Model):
    name = models.CharField(
        verbose_name='Украшение',
        max_length=50
    )
    price = models.FloatField(
        verbose_name='Цена',
        default=0.0
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Декор'
        verbose_name_plural = 'Декор'


class Cake(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    layer = models.OneToOneField(Layer,  on_delete=models.SET_NULL, null=True)
    shape = models.OneToOneField(Shape,  on_delete=models.SET_NULL, null=True)
    topping = models.OneToOneField(Topping, on_delete=models.SET_NULL, null=True, blank=True)
    berries = models.OneToOneField(Berries, on_delete=models.SET_NULL, null=True, blank=True)
    decor = models.OneToOneField(Decor, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(
        verbose_name='Надпись на торте',
        max_length=200,
        blank=True,
        null=True
    )
    ready_to_order = models.BooleanField(default=False)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'


class Complaint(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True
    )
    user = models.ForeignKey(
        Users,
        on_delete=models.SET_NULL,
        null=True
    )

    text = models.TextField(
        verbose_name='Текст сообщения'
    )

    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Обратная связь'
