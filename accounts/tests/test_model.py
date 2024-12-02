from django.test import TestCase
from accounts.models import Cook


class CookModelTest(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create(
            username="testcook",
            first_name="Test",
            last_name="Cook",
            years_of_experience=5
        )

    def test_string_representation(self):
        self.assertEqual(str(self.cook), "testcook (Test Cook)")

    def test_get_absolute_url(self):
        self.assertEqual(
            self.cook.get_absolute_url(),
            f"/accounts/{self.cook.pk}/"
        )
