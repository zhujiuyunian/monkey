# Generated by Django 5.2.2 on 2025-07-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("selling", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sellproduct",
            name="appname",
            field=models.CharField(default="user", max_length=100),
        ),
    ]
