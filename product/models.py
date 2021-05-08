from django.db import models


class Product(models.Model):
    name = models.CharField('Название продукта', max_length=100)
    text = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=0)
    category = models.ForeignKey('category.Category', models.CASCADE, related_name='stuff_category', null=True, blank=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, 'product_image')
    image = models.ImageField('Фото продукта', upload_to='product_image')
