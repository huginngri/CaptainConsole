# Generated by Django 3.0.6 on 2020-05-05 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('orders', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='billing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Billing'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Payment'),
        ),
    ]