# Generated by Django 4.1 on 2022-10-05 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanage', '0041_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Order confirmed', 'Order confirmed'), ('Completed', 'Completed'), ('Returned', 'Returned'), ('Shipped', 'Shipped'), ('Out for Delivery', 'Out for Delivery'), ('Order cancelled', 'Order cancelled')], default='Order confirmed', max_length=150),
        ),
    ]
