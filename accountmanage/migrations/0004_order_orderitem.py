# Generated by Django 4.1 on 2022-09-15 01:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_wishlist'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accountmanage', '0003_alter_useraddress_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('total_price', models.FloatField()),
                ('payment_mode', models.CharField(max_length=150)),
                ('payment_id', models.CharField(max_length=250, null=True)),
                ('status', models.CharField(choices=[('Out for shipping', 'Out for shipping'), ('Pending', 'Pending'), ('Order Placed', 'Order placed'), ('Completed', 'Completed')], default='Pending', max_length=150)),
                ('message', models.TextField(null=True)),
                ('tracking_no', models.CharField(max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountmanage.useraddress')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(null=b'I00\n')),
                ('quantity', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountmanage.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
