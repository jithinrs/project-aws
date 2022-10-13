# Generated by Django 4.1 on 2022-10-11 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanage', '0048_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Returned', 'Returned'), ('Order cancelled', 'Order cancelled'), ('Completed', 'Completed'), ('Shipped', 'Shipped'), ('Out for Delivery', 'Out for Delivery'), ('Order confirmed', 'Order confirmed')], default='Order confirmed', max_length=150),
        ),
    ]