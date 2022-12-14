# Generated by Django 4.1 on 2022-10-18 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanage', '0053_orderitem_prod_disc_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='prod_disc',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Returned', 'Returned'), ('Completed', 'Completed'), ('Shipped', 'Shipped'), ('Order cancelled', 'Order cancelled'), ('Out for Delivery', 'Out for Delivery'), ('Order confirmed', 'Order confirmed')], default='Order confirmed', max_length=150),
        ),
    ]
