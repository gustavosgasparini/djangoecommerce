from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):

    name = models.CharField('Nome', max_length=250)
    slug = models.SlugField('Identificador', max_length=250)

    created = models.DateField('Criado em', auto_now_add=True)
    modified = models.DateField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:category', kwargs={'slug': self.slug})

    class Meta: 
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    
class Product(models.Model):

    name = models.CharField('Nome', max_length=250)
    slug = models.SlugField('Identificador', max_length=250)
    category = models.ForeignKey(Category, verbose_name='Categoria', on_delete=models.CASCADE)
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', max_digits=9, decimal_places=2)

    created = models.DateField('Criado em', auto_now_add=True)
    modified = models.DateField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']