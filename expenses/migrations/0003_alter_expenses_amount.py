# Generated by Django 4.1 on 2022-08-12 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0002_expenses_category_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expenses",
            name="amount",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
