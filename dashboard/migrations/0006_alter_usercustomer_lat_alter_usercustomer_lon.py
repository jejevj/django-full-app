# Generated by Django 4.2.6 on 2023-11-16 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_usercustomer_lat_alter_usercustomer_lon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercustomer',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=-6.1661686, max_digits=9),
        ),
        migrations.AlterField(
            model_name='usercustomer',
            name='lon',
            field=models.DecimalField(decimal_places=6, default=106.8717686, max_digits=9),
        ),
    ]