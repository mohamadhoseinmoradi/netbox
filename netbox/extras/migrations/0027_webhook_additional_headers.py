# Generated by Django 2.2 on 2019-10-13 07:06

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0026_webhook_ca_file_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='webhook',
            name='additional_headers',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]