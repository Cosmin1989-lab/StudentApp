# Generated by Django 5.1 on 2024-08-31 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="age",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
