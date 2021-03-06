# Generated by Django 3.0.6 on 2020-05-06 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consoles', '0001_initial'),
        ('users', '0001_initial'),
        ('manufacturers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=999)),
                ('price', models.FloatField()),
                ('type', models.CharField(max_length=255, null=True)),
                ('rating', models.FloatField()),
                ('console_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consoles.Console')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturers.Manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_content', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.FloatField()),
                ('comment', models.CharField(max_length=999)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=999)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
