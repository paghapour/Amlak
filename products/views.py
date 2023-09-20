from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Product


class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'product'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'