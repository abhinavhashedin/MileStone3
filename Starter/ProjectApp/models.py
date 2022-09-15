from django.db import models

# Create your models here.
#id, description, title, and creator
class Project(models.Model):
    id=models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    title = models.CharField(max_length=20)
    creator =models.CharField(max_length=20)