from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


AGE_CHOICES = (
    ('All', 'All'),  # The first will be in the db and the second will be shown to users
    ('Kids', 'Kids')
)

MOVIE_CHOICES = (
    ('Seasonal', 'Seasonal'),
    ('Single', 'Single')
)


class Profile(models.Model):
    name = models.CharField(max_length=255)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4)


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', blank=True)


class Video(models.Model):
    title = models.CharField(max_length=225, blank=True, null=True)
    file = models.FileField(upload_to='movies')


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(max_length=10, choices=MOVIE_CHOICES)
    movie = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers')
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
