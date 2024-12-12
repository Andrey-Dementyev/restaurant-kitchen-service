from django.urls import path

from kitchen import views


app_name = "kitchen"

urlpatterns = [
    path(
        "",
        views.IndexView.as_view(),
        name="index"
    ),
    path(
        "dish-types/",
        views.DishTypeListView.as_view(),
        name="dish-type-list"
    ),
    path(
        "dish-types/create/",
        views.DishTypeCreateView.as_view(),
        name="dish-type-create"
    ),
    path(
        "dish-types/<int:pk>/update/",
        views.DishTypeUpdateView.as_view(),
        name="dish-type-update"
    ),
    path(
        "dish-types/<int:pk>/delete/",
        views.DishTypeDeleteView.as_view(),
        name="dish-type-delete"
    ),

    path(
        "dishes/",
        views.DishListView.as_view(),
        name="dish-list"
    ),
    path(
        "dishes/<int:pk>/",
        views.DishDetailView.as_view(),
        name="dish-detail"
    ),
    path(
        "dish/create/",
        views.DishCreateView.as_view(),
        name="dish-create"
    ),
    path(
        "dish/<int:pk>/update/",
        views.DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "dish/<int:pk>/delete/",
        views.DishDeleteView.as_view(),
        name="dish-delete"
    ),
    path(
        "dish/<int:pk>/toggle-assign/",
        views.ToggleAssignToDishView.as_view(),
        name="toggle-dish-assign",
    ),
]
