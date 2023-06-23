from django.urls import path, include
from . import views

app_name = "myplant"

urlpatterns = [
    path("", views.home, name="home"),
    path("catalogue/", views.catalogue, name="catalogue"),
    path(
        "profile/",
        include(
            [
                path("create/", views.profile_create, name="profile_create"),
                path(
                    "details/", views.profile_details, name="profile_details"
                ),
                path("edit/", views.profile_edit, name="profile_edit"),
                path("delete/", views.profile_delete, name="profile_delete"),
            ]
        ),
    ),
    path("create/", views.plant_create, name="plant_create"),
    path("details/<int:plant_id>", views.plant_details, name="plant_details"),
    path("edit/<int:plant_id>", views.plant_edit, name="plant_edit"),
    path("delete/<int:plant_id>", views.plant_delete, name="plant_delete"),
]
