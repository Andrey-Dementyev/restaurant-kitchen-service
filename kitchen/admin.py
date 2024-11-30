from django.contrib import admin

from kitchen.models import DishType, Dish


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_filter = ["name",]
    search_fields = ["name",]


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_filter = ["name", "dish_type", "price", "cooks",]
    search_fields = ["name",]
