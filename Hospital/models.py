from django.db import models

class Credentials(models.Model):
    username = models.CharField(max_length=100,unique=True, default="Unknown")
    name = models.CharField(max_length=255, default="Unknown")
    email = models.EmailField(max_length=255,unique=True, default="Unknown")
    phone = models.CharField(max_length=12,default="Unknown")
    password = models.CharField(max_length=255, default="Unknown")
    type=models.CharField(max_length=50,default="Unknown")
    def __str__(self):
        return self.username