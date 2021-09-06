from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Type(models.Model):

    name = models.CharField(max_length=254)
    category = models.ForeignKey('Category', null=True,
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    type = models.ForeignKey('Type', null=True, blank=True,
                             on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    brief_description = models.CharField(max_length=254)
    description = models.TextField(null=True)
    starting_price = models.DecimalField(max_digits=3, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    has_attributes = models.BooleanField (default=False, null=True, blank=True)

    def __str__(self):
        return self.name
