# Generated by Django 3.0.8 on 2020-07-31 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=200)),
                ('Product_price', models.IntegerField(max_length=1000)),
                ('Product_offer', models.IntegerField(max_length=100)),
            ],
        ),
    ]