# Generated by Django 4.1 on 2022-10-22 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanage', '0058_successordermod_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Order cancelled', 'Order cancelled'), ('Shipped', 'Shipped'), ('Out for Delivery', 'Out for Delivery'), ('Order confirmed', 'Order confirmed'), ('Returned', 'Returned'), ('Completed', 'Completed')], default='Order confirmed', max_length=150),
        ),
        migrations.AlterField(
            model_name='successordermod',
            name='order_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accountmanage.order'),
        ),
    ]
