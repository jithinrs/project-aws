# Generated by Django 4.1 on 2022-09-21 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_newcartitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcartitem',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]