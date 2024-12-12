from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Cook


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_filter = UserAdmin.list_filter + ("years_of_experience",)
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "years_of_experience",
                )
            }
        ),
    )
