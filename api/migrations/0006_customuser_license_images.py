# Generated by Django 5.0.1 on 2024-02-02 13:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_customuser_drivers_license'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='license_images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=300, null=True), blank=True, null=True, size=None),
        ),
    ]
