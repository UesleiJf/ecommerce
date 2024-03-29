# Generated by Django 2.1b1 on 2018-08-18 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'Item do Carrinho', 'verbose_name_plural': 'Itens dos Carrinhos'},
        ),
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart_key', 'product')},
        ),
    ]
