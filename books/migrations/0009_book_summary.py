# Generated by Django 2.1.7 on 2021-03-12 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20210307_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.FileField(blank=True, upload_to='summaries/%Y/%m/%d', verbose_name='ملف الفهرس'),
        ),
    ]