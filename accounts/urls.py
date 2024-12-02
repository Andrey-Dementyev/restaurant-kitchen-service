from django.urls import path, include

from accounts import views


app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("activate/<str:uid>/<str:token>/", views.activate, name="activate"),

    path("cooks/", views.CookListView.as_view(), name="cook-list"),
    path("<int:pk>/", views.CookDetailView.as_view(), name="cook-detail"),
    path(
        "<int:pk>/update/",
        views.CookUpdateView.as_view(),
        name="cook-update",
    ),
    path(
        "<int:pk>/delete/",
        views.CookDeleteView.as_view(),
        name="cook-delete",
    ),
]
