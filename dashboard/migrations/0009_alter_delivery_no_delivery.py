# Generated by Django 4.2.6 on 2023-11-16 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='no_delivery',
            field=models.TextField(primary_key=True, serialize=False, unique=True),
        ),
    ]
