# Generated by Django 4.2.1 on 2023-07-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerproductprice',
            name='discount',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Discount'),
        ),
    ]
