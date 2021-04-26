from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from ShopApp.models import Category, Product, Product_Instences, Buyer


# Create your views here.


class CategoriesListView(generic.ListView):
    model = Category


class ProductListView(generic.ListView):
    model = Product


class Product_instancesListView(generic.ListView):
    model = Product_Instences


class BuyersListView(generic.ListView):
    model = Buyer


# Generic Forms

class CategoryAddView(generic.CreateView):
    model = Category
    fields = '__all__'
    # redirect('categories/')


class ProductAddView(generic.CreateView):
    model = Product
    fields = '__all__'
    # redirect('products/')


class ProductInstancesAddView(generic.CreateView):
    model = Product_Instences
    fields = '__all__'


class BuyerAddView(generic.CreateView):
    model = Buyer
    fields = '__all__'
