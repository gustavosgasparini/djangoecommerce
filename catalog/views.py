from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product, Category

# Create your views here.
class ProductListView(ListView):

    model = Product
    template_name = 'catalog/product_list.html'
    paginate_by = 6


class CategoryListView(ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'product_list'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


class ProductsView(ListView):

    template_name = 'catalog/product.html'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, slug=self.kwargs['slug'])
        return context