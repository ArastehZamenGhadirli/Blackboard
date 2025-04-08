from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=20)


class Shape(models.Model):
    pass


class Blackboard(models.Model):
    pass
