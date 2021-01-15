from django.db import models

# Create your models here.
class Querys(models.Model):
    text = models.CharField(max_length=1000)
    date = models.DateField()
    def __str__(self):
        return self.text
