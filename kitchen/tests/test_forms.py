from django.test import TestCase
from django.contrib.auth import get_user_model
from kitchen.forms import DishForm, DishSearchForm, DishTypeSearchForm
from kitchen.models import DishType

User = get_user_model()


class DishFormTest(TestCase):
    def test_dish_form_cooks_field_widget(self):
        form = DishForm()
        self.assertEqual(
            type(form.fields["cooks"].widget).__name__, "CheckboxSelectMultiple"
        )

    def test_dish_form_valid(self):
        dish_type = DishType.objects.create(name="Salad")
        user = User.objects.create_user(username="cook", password="password123")
        form_data = {
            "name": "Greek Salad",
            "description": "Fresh and tasty",
            "price": 10.5,
            "dish_type": dish_type.id,
            "cooks": [user.id],
        }
        form = DishForm(data=form_data)
        self.assertTrue(form.is_valid())


class SearchFormTests(TestCase):
    def test_dish_search_form_placeholder(self):
        form = DishSearchForm()
        self.assertEqual(form.fields["name"].widget.attrs["placeholder"], "Search by name")

    def test_dish_type_search_form_placeholder(self):
        form = DishTypeSearchForm()
        self.assertEqual(form.fields["name"].widget.attrs["placeholder"], "Search by name")
