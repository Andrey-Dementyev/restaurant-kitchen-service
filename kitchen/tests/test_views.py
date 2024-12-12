from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from kitchen.models import DishType, Dish
from accounts.models import Cook

User = get_user_model()


class IndexViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client.login(username="testuser", password="password123")

    def test_index_view(self):
        response = self.client.get(reverse("kitchen:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/index.html")

    def test_index_view_not_logged_in(self):
        response = self.client.get(reverse("kitchen:index"))
        self.assertEqual(response.status_code, 302)


class DishTypeListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client.login(username="testuser", password="password123")
        DishType.objects.create(name="Appetizer")

    def test_dish_type_list_view(self):
        response = self.client.get(reverse("kitchen:dish-type-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")
        self.assertContains(response, "Appetizer")

    def test_create_dish_type_with_missing_data(self):
        response = self.client.post(reverse("kitchen:dish-type-create"), {})
        self.assertEqual(response.status_code, 400)

    def test_update_dish_type_with_invalid_id(self):
        invalid_id = 999
        response = self.client.post(
            reverse("kitchen:dish-type-update", args=[invalid_id]),
            {"name": "Updated Starter"},
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_dish_type_with_invalid_id(self):
        invalid_id = 999
        response = self.client.post(reverse("kitchen:dish-type-delete", args=[invalid_id]))
        self.assertEqual(response.status_code, 404)


class DishListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client.login(username="testuser", password="password123")
        dish_type = DishType.objects.create(name="Appetizer")
        Dish.objects.create(
            name="Spring Rolls",
            price=8.99,
            dish_type=dish_type
        )

    def test_dish_list_view(self):
        response = self.client.get(reverse("kitchen:dish-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_list.html")
        self.assertContains(response, "Spring Rolls")

    def test_create_dish_with_missing_required_field(self):
        response = self.client.post(
            reverse("kitchen:dish-create"),
            {"description": "Incomplete dish"},
        )
        self.assertEqual(response.status_code, 400)

    def test_update_dish_with_invalid_price(self):
        response = self.client.post(
            reverse("kitchen:dish-update", args=[self.dish.id]),
            {"name": "Updated Salad", "price": "invalid_price"},
        )
        self.assertEqual(response.status_code, 400)

    def test_delete_dish_with_invalid_id(self):
        invalid_id = 999
        response = self.client.post(reverse("kitchen:dish-delete", args=[invalid_id]))
        self.assertEqual(response.status_code, 404)


class ToggleAssignToDishTest(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create_user(
            username="cook1",
            password="password123"
        )
        self.dish_type = DishType.objects.create(name="Dessert")
        self.dish = Dish.objects.create(
            name="Cake",
            price=12.99,
            dish_type=self.dish_type
        )
        self.client.login(username="cook1", password="password123")

    def test_toggle_assign_add(self):
        response = self.client.post(
            reverse(
                "kitchen:toggle-dish-assign",
                args=[self.dish.pk]
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn(self.dish, self.cook.dishes.all())

    def test_toggle_assign_remove(self):
        self.cook.dishes.add(self.dish)
        response = self.client.post(
            reverse(
                "kitchen:toggle-dish-assign",
                args=[self.dish.pk]
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(self.dish, self.cook.dishes.all())

    def test_toggle_assign_dish_with_invalid_id(self):
        invalid_id = 999
        response = self.client.post(reverse("kitchen:toggle-dish-assign", args=[invalid_id]))
        self.assertEqual(response.status_code, 404)

    def test_toggle_assign_dish_not_logged_in(self):
        self.client.logout()
        response = self.client.post(reverse("kitchen:toggle-dish-assign", args=[self.dish.id]))
        self.assertEqual(response.status_code, 302)
