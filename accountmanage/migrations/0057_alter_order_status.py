# Generated by Django 4.1 on 2022-10-21 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanage', '0056_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Out for Delivery', 'Out for Delivery'), ('Order cancelled', 'Order cancelled'), ('Shipped', 'Shipped'), ('Order confirmed', 'Order confirmed'), ('Returned', 'Returned')], default='Order confirmed', max_length=150),
        ),
    ]
