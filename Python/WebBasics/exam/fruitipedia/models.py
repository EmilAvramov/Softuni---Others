from django.db import models
from django.core.validators import RegexValidator

start_with_letter = RegexValidator(
    "^[A-Za-z]", "Your name must start with a letter!"
)
only_letters = RegexValidator(
    "^[A-Za-z]+$", "Fruit name should contain only letters!"
)
min_eight_letters = RegexValidator(
    "^.{8,}$", "Field should contain at least 8 symbols"
)
min_two_letters = RegexValidator(
    "^.{2,}$", "Field should contain at least 2 symbols"
)
min_one_letter = RegexValidator(
    "^.{1,}$", "Field should contain at least 1 symbol"
)


class ProfileModel(models.Model):
    first_name = models.CharField(
        verbose_name="First Name",
        max_length=25,
        validators=[start_with_letter, min_two_letters],
    )
    last_name = models.CharField(
        verbose_name="Last Name",
        max_length=35,
        validators=[start_with_letter, min_one_letter],
    )
    email = models.EmailField(verbose_name="Email", max_length=40)
    password = models.CharField(
        verbose_name="Password", max_length=20, validators=[min_eight_letters]
    )
    image_url = models.URLField(verbose_name="Image URL", blank=True)
    age = models.IntegerField(verbose_name="Age", default=18, blank=True)


class FruitModel(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=30,
        validators=[only_letters, min_two_letters],
    )
    image_url = models.URLField(verbose_name="Image URL")
    description = models.TextField(verbose_name="Description")
    nutrition = models.TextField(verbose_name="Nutrition", blank=True)
