from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICES=(
    ('All','All')
    ('Kids', 'Kids')
)

MOVIE_CHOICES=(
    ('seasonal', 'Seasonal')
    ('single', 'Single')
)

class CustomUser(AbstractUser):
    profiles=models.ManyToManyField('Profile', null=True,blank=True)

class Profile(models.Model):
    name=models.CharField(max_length=225)
    age_limit=models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4)

class Movie(models.Model):
    title=models.ChaField(max_length=225)
    description =models.TextField(blanck=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4)
    type=models.CharField(max_length=10, choices=MOVIE_CHOICES)