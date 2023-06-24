from django.urls import path, include
from . import views

app_name = "fruitipedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
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
    path("create/", views.fruit_create, name="fruit_create"),
    path("<int:fruit_id>/details", views.fruit_details, name="fruit_details"),
    path("<int:fruit_id>/edit", views.fruit_edit, name="fruit_edit"),
    path("<int:fruit_id>/delete", views.fruit_delete, name="fruit_delete"),
]
