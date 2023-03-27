from django.db import models

# Create your models here.
class SuperType(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=255)