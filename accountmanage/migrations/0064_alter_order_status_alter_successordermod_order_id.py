# Generated by Django 4.1 on 2022-10-22 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanage', '0063_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Out for Delivery', 'Out for Delivery'), ('Shipped', 'Shipped'), ('Order cancelled', 'Order cancelled'), ('Returned', 'Returned'), ('Order confirmed', 'Order confirmed')], default='Order confirmed', max_length=150),
        ),
        migrations.AlterField(
            model_name='successordermod',
            name='order_id',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
