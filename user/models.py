from django.db import models
from django.conf import settings


class Profiles(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE, related_name='profile', null=True)
    name = models.CharField('Имя', max_length=100, null=True, blank=True)
    last_name = models.CharField('Фамилия', max_length=100, blank=True, null=True)
    birthday = models.DateField('Дата рождения', blank=True, null=True)
    balance = models.PositiveIntegerField('Баланс', default=0, null=True)
    phone = models.CharField('Номер телефона', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Stuff(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE, related_name='stuff', null=True)
    name = models.CharField('Имя', max_length=100, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.name} {self.last_name}'
