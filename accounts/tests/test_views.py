from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
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
