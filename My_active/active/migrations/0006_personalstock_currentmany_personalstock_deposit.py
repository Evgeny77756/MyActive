# Generated by Django 4.1.7 on 2023-05-04 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('active', '0005_personalstock_totalcountamd_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalstock',
            name='currentMany',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='personalstock',
            name='deposit',
            field=models.FloatField(default=0),
        ),
    ]
