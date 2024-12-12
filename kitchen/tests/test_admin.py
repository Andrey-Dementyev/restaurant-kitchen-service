from django.test import TestCase
from django.contrib.admin.sites import site
from kitchen.models import DishType, Dish
from kitchen.admin import DishTypeAdmin, DishAdmin


class KitchenAdminTest(TestCase):
    def test_dish_type_admin_registered(self):
        self.assertIn(DishType, site._registry)
        self.assertIsInstance(site._registry[DishType], DishTypeAdmin)

    def test_dish_admin_registered(self):
        self.assertIn(Dish, site._registry)
        self.assertIsInstance(site._registry[Dish], DishAdmin)

    def test_dish_type_admin_customizations(self):
        admin_instance = site._registry[DishType]
        self.assertIn("name", admin_instance.search_fields)
        self.assertIn("name", admin_instance.list_filter)

    def test_dish_admin_customizations(self):
        admin_instance = site._registry[Dish]
        self.assertIn("name", admin_instance.search_fields)
        self.assertIn("price", admin_instance.list_filter)
