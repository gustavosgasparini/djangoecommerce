from django.db import models
from django.conf import settings

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


class OrderManager(models.Manager):

    def create_order(self, user, cart_items):
        order = self.create(user=user)
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(
                order=order, quantity=cart_item.quantity, product=cart_item.product, price=cart_item.price,
            )
        return order


class Order(models.Model):

    STATUS_CHOICES = (
        (0, 'Aguardando pagamento'),
        (1, 'Concluída'),
        (2, 'Cancelada'),
    )

    PAYMENT_OPTION_CHOICES = (
        ('deposit', 'Depósito'),
        ('pagseguro', 'PagSeguro'),
        ('paypal', 'PayPal'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', on_delete=models.CASCADE)
    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES, default=0, blank=True,
    )
    payment_option = models.CharField(
        'Opção de pagamento', choices=PAYMENT_OPTION_CHOICES, max_length=50, default='deposit',
    )
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    objects = OrderManager()

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f'Pedido #{self.pk}'

    
class OrderItem(models.Model):

    order = models.ForeignKey(Order, verbose_name='Pedido', related_name='Items', on_delete=models.CASCADE)
    product = models.ForeignKey('catalog.Product', verbose_name='Produto', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', max_digits=9, decimal_places=2)

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens dos pedidos'

    def __str__(self):
        return f'[{self.order}] {self.product}'


def post_save_cart_item(instance, **kwargs):
    if instance.quantity < 1:
        instance.delete()

models.signals.post_save.connect(
    post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item'
)
