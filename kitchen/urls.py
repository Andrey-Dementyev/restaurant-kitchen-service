from django.urls import path

from kitchen import views


app_name = "kitchen"

urlpatterns = [
    path("", views.index, name="index"),
    path("dish-types/", views.DishTypeListView.as_view(), name="dish-type-list"),
    path("dishes/", views.DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", views.DishDetailView.as_view(), name="dish-detail"),

]
