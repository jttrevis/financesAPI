from django.db import models


class Expenses(models.Model):
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=20, decimal_places=20)
