from django.db import models
from category.models import *


class Expenses(models.Model):
    CATEGORY_ID = CategoryAPI.CAT_OPT
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # category_name = models.ForeignKey(
    #     CategoryAPI, related_name='expenses', on_delete=models.CASCADE, null=False, default='O')
    category_opt = models.CharField(
        choices=CATEGORY_ID, max_length=1, null=False, default='O')
