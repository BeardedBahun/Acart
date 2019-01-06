from django.db import models
from autoslug import AutoSlugField  # no need to add autoslug
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=70)
    slug = AutoSlugField(populate_from='title', unique=True)
    image = ImageField()
    description = RichTextField()


class Product(models.Model):
    title = models.CharField
    slug = AutoSlugField(populate_from='title', unique=True)
    description = RichTextField()
    price = models.DecimalField(max_digits=9999999999, decimal_places=2)
    brand = models.CharField(max_length=70)
    discount = models.BooleanField()


class ProductHasImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = ImageField()


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #
    rating = models.IntegerField()
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
