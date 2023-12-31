from django.contrib import admin

from bake_cake_bot.models import *


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'telegram_id', 'username', 'name']
    search_fields = ['telegram_id', 'username', 'phone']

@admin.register(Order)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['number', 'username', 'price', 'init_date', 'delivery_date']


@admin.register(Cake)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'layer', 'shape', 'topping', 'berries', 'decor', 'price']


@admin.register(Layer)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(Shape)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(Topping)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(Berries)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(Decor)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(Complaint)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['order', 'user', 'text']