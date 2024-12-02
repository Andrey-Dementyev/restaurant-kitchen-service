from django.test import TestCase
from django.contrib.admin.sites import site
from accounts.models import Cook


class CookAdminTest(TestCase):
    def test_cook_admin_registered(self):
        self.assertIn(Cook, site._registry)

    def test_cook_admin_customizations(self):
        cook_admin = site._registry[Cook]
        self.assertEqual(cook_admin.list_filter[-1], "years_of_experience")
        self.assertIn("years_of_experience", cook_admin.list_display)
