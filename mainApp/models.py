from django.db import models


class Signin(models.Model):
    email = models.EmailField()


class Signup(models.Model):
    firstName = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

class Ticket(models.Model):
    genre = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
