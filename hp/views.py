from django.shortcuts import render
from django.views.generic import ListView,DetailView
from hp.models import Product
# Create your views here.
class ProductLV(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductDV(DetailView):
    model = Product
    template_name = 'product_detail.html'
