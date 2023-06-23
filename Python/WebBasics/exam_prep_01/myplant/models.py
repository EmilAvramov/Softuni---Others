from django.db import models
from django.core.validators import RegexValidator

start_with_capital = RegexValidator(
    "^[A-Z].*", "Your name must start with a capital letter!"
)
min_two_letters = RegexValidator("^.{2,}$")
only_letters = RegexValidator(
    "^[A-Za-z]+$", "Plant name should contain only letters!"
)


class Profile(models.Model):
    username = models.CharField(
        verbose_name="Username",
        max_length=10,
        blank=False,
        unique=True,
        validators=[min_two_letters],
    )
    first_name = models.CharField(
        verbose_name="First name",
        max_length=20,
        blank=False,
        validators=[start_with_capital],
    )
    last_name = models.CharField(
        verbose_name="Last Name",
        max_length=20,
        blank=False,
        validators=[start_with_capital],
    )
    profile_picture = models.URLField("Profile Picture", null=True, blank=True)


TYPE = (
    ("Outdoor Plants", "Outdoor Plants"),
    ("Indoor Plants", "Indoor Plants"),
)


class Plant(models.Model):
    plant_type = models.CharField(
        verbose_name="Plant Type", max_length=14, blank=False, choices=TYPE,
    )
    name = models.CharField(
        verbose_name="Name",
        max_length=20,
        blank=False,
        validators=[min_two_letters, only_letters],
    )
    image_url = models.URLField(verbose_name="Image Url")
    description = models.TextField(verbose_name="Description")
    price = models.FloatField(verbose_name="Price")
