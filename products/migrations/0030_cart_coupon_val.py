# Generated by Django 4.1 on 2022-10-04 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_alter_coupon_valid_from_alter_coupon_valid_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon_val',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
