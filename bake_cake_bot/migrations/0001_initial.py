# Generated by Django 4.2.3 on 2023-07-26 16:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('telegram_id', models.IntegerField(default=False, unique=True)),
                ('username', models.CharField(max_length=64, null=True, verbose_name='User Name')),
                ('first_name', models.CharField(max_length=256, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Last Name')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='email')),
                ('is_admin', models.BooleanField(blank=True, default=False, null=True, verbose_name='Администратор')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
