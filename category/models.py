from django.db import models


class CategoryAPI(models.Model):

    CAT_OPT = [
        ('Food', 'Food'),
        ('Health', 'Health'),
        ('Education', 'Education'),
        ('Home', 'Home'),
        ('Other', 'Other'),
    ]
    category_type = models.CharField(choices=CAT_OPT, max_length=20)
