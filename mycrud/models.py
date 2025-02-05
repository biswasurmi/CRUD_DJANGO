from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField()
    course = models.TextField(default="Unknown")
    