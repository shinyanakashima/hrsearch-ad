from django.db import models

# Create your models here.

class Promotion(models.Model):
    sponsored = models.TextField()
    url = models.TextField()
    date = models.TextField()
    title = models.TextField()
    content = models.TextField()
    site = models.TextField()
