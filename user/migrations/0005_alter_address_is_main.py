# Generated by Django 4.0.5 on 2022-08-30 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_address_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='is_main',
            field=models.BooleanField(blank=True),
        ),
    ]
