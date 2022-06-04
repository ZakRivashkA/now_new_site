from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_created=True, null=True, blank=True)
    update = models.DateTimeField(auto_now=True, null=True, blank=True)
    categories = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Shop(models.Model):
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    street = models.CharField(max_length=250)
    products = models.ManyToManyField('Product')

    def __str__(self):
        return self.name
