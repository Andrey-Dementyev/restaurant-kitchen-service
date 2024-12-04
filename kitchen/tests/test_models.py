from django.test import TestCase
from kitchen.models import DishType, Dish


class DishTypeModelTest(TestCase):
    def test_string_representation(self):
        dish_type = DishType.objects.create(name="Appetizer")
        self.assertEqual(str(dish_type), "Appetizer")


class DishModelTest(TestCase):
    def test_string_representation(self):
        dish_type = DishType.objects.create(name="Dessert")
        dish = Dish.objects.create(
            name="Ice Cream",
            price=5.99,
            dish_type=dish_type
        )
        self.assertEqual(str(dish), "Ice Cream (price: 5.99)")
