# Generated by Django 2.2.4 on 2020-12-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktioneryapp', '0013_remove_order_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(null=True),
        ),
    ]
