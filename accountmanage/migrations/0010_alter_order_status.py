# Generated by Django 4.1 on 2022-09-16 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanage', '0009_alter_order_email_alter_order_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Order Placed', 'Order placed'), ('Completed', 'Completed'), ('Pending', 'Pending'), ('Out for shipping', 'Out for shipping')], default='Pending', max_length=150),
        ),
    ]
