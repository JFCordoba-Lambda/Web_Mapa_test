from django.db import models
# Create your models here.

class Search(models.Model):
    date = models.DateTimeField(auto_now_add=True)

