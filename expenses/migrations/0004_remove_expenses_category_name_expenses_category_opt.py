# Generated by Django 4.1 on 2022-08-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0003_alter_expenses_amount"),
    ]

    operations = [
        migrations.RemoveField(model_name="expenses", name="category_name",),
        migrations.AddField(
            model_name="expenses",
            name="category_opt",
            field=models.CharField(
                choices=[
                    ("F", "Food"),
                    ("H", "Health"),
                    ("E", "Education"),
                    ("H", "Home"),
                    ("O", "Other"),
                ],
                default="O",
                max_length=1,
            ),
        ),
    ]