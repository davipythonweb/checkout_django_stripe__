# Generated by Django 4.2.14 on 2024-07-15 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_order_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='value',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]
