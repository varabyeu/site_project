from django.db import models

class User(models.Model):
    name = models.CharField(verbose_name='name', max_length=100)

# Create your models here.
