# Generated by Django 2.1.7 on 2019-12-30 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='الإسم'),
        ),
    ]
