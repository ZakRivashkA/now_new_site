from django.db import models


class Droid(models.Model):
    name = models.CharField(max_length=20)
    master = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images', null=False, blank=True)
