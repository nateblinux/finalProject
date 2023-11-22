from django.db import models

class Signin(models.Model):
    firstName = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
