from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from kitchen.models import DishType, Dish
from accounts.models import Cook

User = get_user_model()


class IndexViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")

    def test_index_view(self):
        response = self.client.get(reverse("kitchen:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/index.html")


class DishTypeListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")
        DishType.objects.create(name="Appetizer")

    def test_dish_type_list_view(self):
        response = self.client.get(reverse("kitchen:dish-type-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")
        self.assertContains(response, "Appetizer")


class DishListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")
        dish_type = DishType.objects.create(name="Appetizer")
        Dish.objects.create(name="Spring Rolls", price=8.99, dish_type=dish_type)

    def test_dish_list_view(self):
        response = self.client.get(reverse("kitchen:dish-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_list.html")
        self.assertContains(response, "Spring Rolls")


class ToggleAssignToDishTest(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create_user(username="cook1", password="password123")
        self.dish_type = DishType.objects.create(name="Dessert")
        self.dish = Dish.objects.create(name="Cake", price=12.99, dish_type=self.dish_type)
        self.client.login(username="cook1", password="password123")

    def test_toggle_assign_add(self):
        response = self.client.post(reverse("kitchen:toggle-dish-assign", args=[self.dish.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertIn(self.dish, self.cook.dishes.all())

    def test_toggle_assign_remove(self):
        self.cook.dishes.add(self.dish)
        response = self.client.post(reverse("kitchen:toggle-dish-assign", args=[self.dish.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(self.dish, self.cook.dishes.all())
