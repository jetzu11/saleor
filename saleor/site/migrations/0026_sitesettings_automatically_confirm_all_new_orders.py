# Generated by Django 3.1.2 on 2020-11-03 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("site", "0025_auto_20191024_0552"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitesettings",
            name="automatically_confirm_all_new_orders",
            field=models.BooleanField(default=True),
        ),
    ]
