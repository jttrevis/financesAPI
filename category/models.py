from django.db import models


class CategoryAPI(models.Model):

    CAT_OPT = [
        ('F', 'Food'),
        ('H', 'Health'),
        ('E', 'Education'),
        ('H', 'Home'),
        ('O', 'Other'),
    ]
    category_type = models.CharField(
        choices=CAT_OPT, max_length=1, null=False, default='O')
