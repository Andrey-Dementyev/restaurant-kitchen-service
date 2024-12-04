from django.test import TestCase
from accounts.forms import RegisterForm, CookUpdateForm, CookSearchForm


class RegisterFormTest(TestCase):
    def test_register_form_valid(self):
        form = RegisterForm(data={
            "username": "testuser",
            "password1": "strongpassword123",
            "password2": "strongpassword123",
            "email": "test@example.com"
        })
        self.assertTrue(form.is_valid())

    def test_register_form_invalid_email(self):
        form = RegisterForm(data={
            "username": "testuser",
            "password1": "strongpassword123",
            "password2": "strongpassword123",
            "email": "invalid-email"
        })
        self.assertFalse(form.is_valid())


class CookUpdateFormTest(TestCase):
    def test_cook_update_form_fields(self):
        form = CookUpdateForm()
        self.assertEqual(
            list(form.fields.keys()),
            ["first_name", "last_name", "years_of_experience"]
        )


class CookSearchFormTest(TestCase):
    def test_cook_search_form_placeholder(self):
        form = CookSearchForm()
        self.assertEqual(
            form.fields["username"].widget.attrs["placeholder"],
            "Search by username"
        )
