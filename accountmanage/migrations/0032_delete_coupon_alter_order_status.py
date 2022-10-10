# Generated by Django 4.1 on 2022-10-03 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanage', '0031_coupon_alter_order_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coupon',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out for Delivery', 'Out for Delivery'), ('Returned', 'Returned'), ('Order confirmed', 'Order confirmed'), ('Order cancelled', 'Order cancelled'), ('Shipped', 'Shipped'), ('Completed', 'Completed')], default='Order confirmed', max_length=150),
        ),
    ]