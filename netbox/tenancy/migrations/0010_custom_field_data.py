# Generated by Django 3.1 on 2020-08-21 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenancy', '0009_standardize_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='custom_field_data',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
