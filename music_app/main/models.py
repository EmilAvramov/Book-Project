from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models

# Create your models here.
class Profile(models.Model):
    USERNAME_MIN_LENGTH = 2
    USERNAME_MAX_LENGTH = 15

    username = models.CharField(
        verbose_name="Username",
        validators=[
            MinLengthValidator(
                USERNAME_MIN_LENGTH, "Username must be at least 2 characters."
            ),
            RegexValidator(
                r"[A-Za-z0-9_]+",
                "Username must contain letters, numbers or _ only.",
            ),
        ],
        max_length=USERNAME_MAX_LENGTH,
    )
    email = models.EmailField(verbose_name="Email")
    age = models.PositiveIntegerField(verbose_name="Age", null=True,)


class Album(models.Model):
    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_NAME_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30

    GENRE_CHOICES = [
        (x, x)
        for x in (
            "Pop Music",
            "Jazz Music",
            "R&B Music",
            "Rock Music",
            "Country Music",
            "Dance Music",
            "Hip Hop Music",
            "Other",
        )
    ]

    album_name = models.CharField(
        verbose_name="Album Name",
        null=False,
        unique=True,
        max_length=ALBUM_NAME_MAX_LENGTH,
    )

    artist = models.CharField(
        verbose_name="Artist Name", max_length=ARTIST_NAME_MAX_LENGTH
    )

    genre = models.CharField(
        verbose_name="Genre",
        max_length=GENRE_MAX_LENGTH,
        choices=GENRE_CHOICES,
    )
    description = models.TextField(verbose_name="Description", null=True,)
    image_url = models.ImageField(verbose_name="Image URL")
    price = models.FloatField(
        validators=[MinValueValidator(0.0, 'Value must be above 0.')]
    )