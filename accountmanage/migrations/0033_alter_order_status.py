# Generated by Django 4.1 on 2022-10-03 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanage', '0032_delete_coupon_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Shipped', 'Shipped'), ('Order confirmed', 'Order confirmed'), ('Out for Delivery', 'Out for Delivery'), ('Returned', 'Returned'), ('Completed', 'Completed'), ('Order cancelled', 'Order cancelled')], default='Order confirmed', max_length=150),
        ),
    ]
