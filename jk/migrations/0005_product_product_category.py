# Generated by Django 3.0.8 on 2020-08-03 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jk', '0004_auto_20200731_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Product_category',
            field=models.CharField(max_length=100),
            preserve_default=False,
        ),
    ]
