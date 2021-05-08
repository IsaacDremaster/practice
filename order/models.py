from django.db import models
from django.db.models import F, Sum

from product.models import Product

from decimal import Decimal


class Order(models.Model):
    CHOICES = (
        ('1', 'New'),
        ('2', 'Courier appointed'),
        ('3', 'On the way'),
        ('4', 'Delivered'),
        ('5', 'Canceled'),
    )

    customer = models.ForeignKey('user.Profiles', models.SET_NULL, related_name='customer_order', null=True)
    date = models.DateTimeField('Дата заказа', auto_now_add=True, null=True)
    total = models.DecimalField('Итого', max_digits=10, decimal_places=0, default=0, blank=True, null=True)
    status = models.CharField(max_length=100, choices=CHOICES, default=1)
    quantity = models.IntegerField(default=0)

    def set_total_price(self):
        self.total = self.product_order_product.all().aggregate(total=Sum(F('good_quantity') * F('product__price')))['total']
        self.save()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, models.SET_NULL, null=True)
    order = models.ForeignKey(Order, models.CASCADE, 'product_order_product', null=True)
    product_quantity = models.PositiveSmallIntegerField('Количество товара', default=1)

    class Meta:
        verbose_name = 'Заказ продукта'
        verbose_name_plural = 'Заказы продуктов'
