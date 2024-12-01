from django.urls import path, include

from accounts import views


app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("cooks/", views.CookListView.as_view(), name="cook-list"),
    path("<int:pk>/", views.CookDetailView.as_view(), name="cook-detail"),
]
