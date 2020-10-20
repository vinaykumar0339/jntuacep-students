from django.db import models

# Create your models here.
class Register(models.Model):
    roll_number = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username