# Generated by Django 3.0.3 on 2020-02-21 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
    ]
