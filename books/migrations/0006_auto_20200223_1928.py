# Generated by Django 2.1.7 on 2020-02-23 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20200223_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='الثمن'),
        ),
    ]
