# Generated by Django 4.1 on 2022-08-12 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0006_remove_expenses_category_opt_expenses_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expenses", name="date", field=models.DateField(auto_now=True),
        ),
    ]