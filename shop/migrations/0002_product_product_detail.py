# Generated by Django 3.0.3 on 2020-02-17 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
