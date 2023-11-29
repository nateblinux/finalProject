from django.db import models
from django.conf import settings


class Signin(models.Model):
    email = models.EmailField()


class Signup(models.Model):
    firstName = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

class Ticket(models.Model):
    genre = models.CharField(max_length=200)
    city = models.CharField(max_length=200)


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    eventId = models.CharField(max_length=15)

