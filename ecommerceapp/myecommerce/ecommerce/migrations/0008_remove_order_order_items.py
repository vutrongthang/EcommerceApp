# Generated by Django 4.1.7 on 2023-04-24 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_order_order_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_items',
        ),
    ]