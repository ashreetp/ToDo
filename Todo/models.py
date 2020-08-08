from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.username

class List(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    description = models.TextField(max_length=10000)
    
    def __str__(self):
        return self.username
