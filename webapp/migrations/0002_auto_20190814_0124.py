# Generated by Django 2.2.4 on 2019-08-14 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project',
            new_name='Product',
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
    ]
