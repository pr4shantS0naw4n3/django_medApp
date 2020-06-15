from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class User(models.Model):
    firstName=models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    emailId=models.EmailField(unique=True,blank=False)
    password=models.CharField(max_length=30,blank=False)
    dateOfBirth=models.DateField(blank=False)
    city = models.CharField(max_length=30,blank=False)
    state = models.CharField(max_length=30,blank=False)
    country = models.CharField(max_length=30,blank=False)
    adminRoleType = models.CharField(max_length=30,blank=False)
    isActive=models.BooleanField(blank=True,default=False)

