# Generated by Django 5.0.6 on 2024-06-20 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_category_alter_product_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_images', to='shop.product'),
        ),
    ]
