from django.db import models


# Create your models here.
class Paco(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default="")
    has_a_gun = models.BooleanField(default=True)
    like_donuts = models.BooleanField(default=True)
    waste_time = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name

