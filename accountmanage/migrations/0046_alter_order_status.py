# Generated by Django 4.1 on 2022-10-08 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanage', '0045_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Order cancelled', 'Order cancelled'), ('Order confirmed', 'Order confirmed'), ('Returned', 'Returned'), ('Shipped', 'Shipped'), ('Completed', 'Completed'), ('Out for Delivery', 'Out for Delivery')], default='Order confirmed', max_length=150),
        ),
    ]
