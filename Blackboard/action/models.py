from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=10)

class Blackboard(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
        
    )
    code = models.PositiveIntegerField(null=False , primary_key=True)
    


class Image(models.Model):
    image_name = models.CharField(max_length=20)
    image_height = models.IntegerField()
    image_width = models.IntegerField()
    black_board = models.ForeignKey(to=Blackboard , related_name="Image_Blackboard" , on_delete=models.CASCADE)
    
    
class Text(models.Model):
    content = models.TextField(max_length=500)
    font_size = models.PositiveIntegerField()
    colors ={
        "red" : "Red",
        "black" : "Black",
        "blue" : "Blue"
    }
    
    font_color = models.CharField(max_length=20 , choices=colors , default="black")
    black_board = models.ForeignKey(to=Blackboard , related_name="Text_Blackboard" , on_delete=models.CASCADE)
    
    
