from django.db import models

# Create your models here.
class Sample(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
