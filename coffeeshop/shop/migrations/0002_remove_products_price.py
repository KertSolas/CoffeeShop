# Generated by Django 4.2.5 on 2023-10-09 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
    ]
