# Generated by Django 4.2.3 on 2023-07-30 17:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bake_cake_bot', '0004_alter_users_options_alter_users_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Berries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ягоды')),
                ('price', models.FloatField(default=0.0, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Decor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Украшение')),
                ('price', models.FloatField(default=0.0, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Слой')),
                ('price', models.FloatField(default=0.0, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Форма')),
                ('price', models.FloatField(default=0.0, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Топпинг')),
                ('price', models.FloatField(default=0.0, verbose_name='Цена')),
            ],
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Номер заказа')),
                ('price', models.FloatField(default=0.0, verbose_name='Цена')),
                ('init_date', models.DateTimeField(default=datetime.datetime(2023, 7, 30, 17, 7, 30, 383954, tzinfo=datetime.timezone.utc), verbose_name='Дата создания заказа')),
                ('delivery_date', models.DateTimeField(default=None, verbose_name='Дата и время доставки')),
                ('address', models.TextField(max_length=500, verbose_name='Адрес доставки')),
                ('promocode', models.CharField(blank=True, max_length=100, verbose_name='Промокод')),
                ('comment', models.TextField(blank=True, max_length=1000, verbose_name='Комментарий')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bake_cake_bot.users')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст сообщения')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bake_cake_bot.order')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bake_cake_bot.users')),
            ],
        ),
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('text', models.TextField(blank=True, max_length=200, verbose_name='Надпись на торте')),
                ('ready_to_order', models.BooleanField(default=False)),
                ('price', models.FloatField(default=0.0)),
                ('berries', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bake_cake_bot.berries')),
                ('decor', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bake_cake_bot.decor')),
                ('layer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bake_cake_bot.layer')),
                ('shape', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bake_cake_bot.shape')),
                ('topping', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bake_cake_bot.topping')),
            ],
        ),
    ]
