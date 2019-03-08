# Generated by Django 2.1.7 on 2019-03-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_option',
            field=models.CharField(choices=[('deposit', 'Depósito'), ('pagseguro', 'PagSeguro'), ('paypal', 'PayPal')], default='deposit', max_length=50, verbose_name='Opção de pagamento'),
        ),
    ]
