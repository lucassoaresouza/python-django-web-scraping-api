# Generated by Django 2.2.4 on 2019-08-15 14:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=350), size=None)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
