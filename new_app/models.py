from django.db import models


class Person(models.Model):
    nickname = models.CharField(max_length=10)
    login = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='image_person')

    def __str__(self):
        return self.nickname
