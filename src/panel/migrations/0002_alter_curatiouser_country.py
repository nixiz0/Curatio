# Generated by Django 4.2.7 on 2023-11-05 22:31

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curatiouser',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]