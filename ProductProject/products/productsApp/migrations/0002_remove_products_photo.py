# Generated by Django 5.0 on 2024-01-05 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productsApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='Photo',
        ),
    ]
