# Generated by Django 4.2.5 on 2023-10-09 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_coffeename_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeename',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
