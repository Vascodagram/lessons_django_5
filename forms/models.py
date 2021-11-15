from django.db import models
from django.http import HttpRequest, HttpResponse
# Create your models here.


class FormCompany(models.Model):
    CHOICES_COMPANY = (
        ('epam', 'EPAM'),
        ('logic', 'Logic'),
        ('rozetka', 'Rozetka'),
    )

    name = models.CharField(max_length=200, verbose_name='Имя ')
    surname = models.CharField(max_length=200, verbose_name='Фамилия ')
    age = models.IntegerField('Возраст')
    company = models.CharField(choices=CHOICES_COMPANY, max_length=200, verbose_name='Компания ')
    salary = models.IntegerField('Зарплата')