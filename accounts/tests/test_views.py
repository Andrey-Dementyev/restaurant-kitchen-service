from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from accounts.models import Cook

User = get_user_model()


class RegisterViewTest(TestCase):
    def test_register_get(self):
        response = self.client.get(reverse("accounts:register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")

    def test_register_post_valid(self):
        response = self.client.post(reverse("accounts:register"), {
            "username": "newuser",
            "password1": "strongpassword123",
            "password2": "strongpassword123",
            "email": "newuser@example.com"
        })
        self.assertRedirects(response, reverse("accounts:login"))
        self.assertEqual(User.objects.filter(username="newuser").count(), 1)

    def test_register_with_missing_data(self):
        response = self.client.post(reverse("accounts:register"), {"username": ""})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")

    def test_register_with_duplicate_email(self):
        User.objects.create_user(username="existinguser", email="test@example.com", password="password123")
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "newuser",
                "email": "test@example.com",
                "password1": "password123",
                "password2": "password123",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User with this Email already exists.")


class ActivationViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password123", is_active=False
        )
        self.uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        self.token = "invalid_token"

    def test_activation_with_invalid_token(self):
        response = self.client.get(
            reverse("accounts:activate", args=[self.uid, self.token])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Activation link is invalid!")

    def test_activation_with_invalid_uid(self):
        invalid_uid = "invalid_uid"
        response = self.client.get(
            reverse("accounts:activate", args=[invalid_uid, self.token])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Activation link is invalid!")


class CookListViewTest(TestCase):
    def setUp(self):
        self.user = Cook.objects.create_user(
            username="cook1",
            password="password123"
        )

    def test_cook_list_view(self):
        self.client.login(username="cook1", password="password123")
        response = self.client.get(reverse("accounts:cook-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/cook_list.html")


class CookDetailViewTest(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create_user(
            username="cook1",
            password="password123"
        )

    def test_cook_detail_view(self):
        self.client.login(username="cook1", password="password123")
        response = self.client.get(
            reverse(
                "accounts:cook-detail",
                kwargs={"pk": self.cook.pk}
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/cook_detail.html")
