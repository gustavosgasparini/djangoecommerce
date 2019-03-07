from django.db import models

# Create your models here.
class CartIemManager(models.Manager):

    def add_item(self, cart_key, product):
        if self.filter(cart_key=cart_key, product=product).exists():
            created = False
            cart_item = self.get(cart_key=cart_key, product=product)
            cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
        else:
            created = True
            cart_item = CartItem.objects.create(cart_key=cart_key, product=product, price=product.price)
        return cart_item, created


class CartItem(models.Model):
    
    cart_key = models.CharField('Chave do carrinho', max_length=40, db_index=True)
    product = models.ForeignKey('catalog.Product', verbose_name='Produto', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', max_digits=9, decimal_places=2)

    objects = CartIemManager()

    class Meta:
        verbose_name = 'Item do carrinho'
        verbose_name_plural = 'Itens dos carrinhos'
        unique_together = (('cart_key', 'product'),)
    
    def __str__(self):
        return f'{self.product} [{self.quantity}]'
