from django.db import models


# Create your models here.
class Paco(models.Model):
    name = models.CharField(max_length=100)
    has_a_gun = models.BooleanField()

    def __str__(self):
        return self.name


