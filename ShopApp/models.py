from django.db import models
import uuid
from django.urls import reverse


# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Category Name')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories')

class Product(models.Model):
    product_Name = models.CharField(max_length=200, help_text='Product Name')
    body = models.TextField(max_length=1500, help_text='Product Detail')
    type = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_Name

    def get_absolute_url(self):
        return reverse('products')


class Product_Instences(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    Instences_title = models.CharField(max_length=200)
    Instences_description = models.CharField(max_length=200)
    Buyer = models.ForeignKey('Buyer', on_delete=models.SET_NULL, null=True)
    Type = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.Instences_title

    class Meta:
        verbose_name_plural='Product Instences'

    def get_absolute_url(self):
        return reverse('product_instences')

class Buyer(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Contact_number = models.CharField(max_length=22)
    Email = models.EmailField()
    Address = models.TextField(max_length=500)
    Note = models.TextField(max_length=1000)

    def __str__(self):
        return "{} {} {} {}".format(self.First_Name, self.Last_Name, self.Contact_number, self.Email)

    def get_absolute_url(self):
        return reverse('buyers')
