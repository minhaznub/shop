from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('categories/', views.CategoriesListView.as_view(), name='categories'),
    path('', views.CategoriesListView.as_view(), name='categories'),
    path('products', views.ProductListView.as_view(), name='products'),
    path('buyers', views.BuyersListView.as_view(), name='buyers'),
    path('product_instences', views.Product_instancesListView.as_view(), name='product_instences'),
    # path('Category', views.Product_instancesListView.as_view(), name='product_instences'),

    path('category-add', views.CategoryAddView.as_view(), name='category-add'),
    path('product-add', views.ProductAddView.as_view(), name='product-add'),
    path('product_instences-add', views.ProductInstancesAddView.as_view(), name='product_instences-add'),
    path('buyer-add', views.BuyerAddView.as_view(), name='buyer-add'),
]
