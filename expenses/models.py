
from django.db import models
from category.models import *
from django_filters import rest_framework as filters


class Expenses(models.Model):
    CATEGORY_ID = CategoryAPI.CAT_OPT
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category_opt = models.CharField(
        choices=CATEGORY_ID, max_length=10, null=False, default='Other', name='category')
