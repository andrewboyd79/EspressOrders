from django.db import models


class Location(models.Model):

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Cart(models.Model):

    name = models.CharField(max_length=254, default="cart")
    location = models.ForeignKey('Location', null=True,
                                 on_delete=models.SET_NULL)
    location_description = models.CharField(max_length=254)
    barista = models.CharField(max_length=254)
    opening_times = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
