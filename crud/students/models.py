from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=50)
    dept=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)
   