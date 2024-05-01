from django.db import models


class User(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.IntegerField()
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
