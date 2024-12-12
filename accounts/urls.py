from django.urls import path, include

from accounts import views


app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path(
        "register/",
        views.RegisterView.as_view(),
        name="register"
    ),
    path(
        "activate/<str:uid>/<str:token>/",
        views.ActivateAccountView.as_view(),
        name="activate"
    ),

    path(
        "cooks/",
        views.CookListView.as_view(),
        name="cook-list"
    ),
    path(
        "cooks/<int:pk>/",
        views.CookDetailView.as_view(),
        name="cook-detail"
    ),
    path(
        "cooks/<int:pk>/update/",
        views.CookUpdateView.as_view(),
        name="cook-update",
    ),
    path(
        "cooks/<int:pk>/delete/",
        views.CookDeleteView.as_view(),
        name="cook-delete",
    ),
]
