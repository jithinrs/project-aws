# Generated by Django 4.1 on 2022-10-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanage', '0066_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Returned', 'Returned'), ('Order confirmed', 'Order confirmed'), ('Out for Delivery', 'Out for Delivery'), ('Order cancelled', 'Order cancelled'), ('Shipped', 'Shipped'), ('Completed', 'Completed')], default='Order confirmed', max_length=150),
        ),
    ]
