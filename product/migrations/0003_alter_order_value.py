# Generated by Django 4.2.14 on 2024-07-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_price_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='value',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]
