# Generated by Django 4.1 on 2022-09-15 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanage', '0007_alter_order_address_1_alter_order_address_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default='1', max_length=256),
        ),
        migrations.AddField(
            model_name='order',
            name='mobile',
            field=models.CharField(default='1', max_length=256),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Order Placed', 'Order placed'), ('Pending', 'Pending'), ('Out for shipping', 'Out for shipping')], default='Pending', max_length=150),
        ),
    ]
