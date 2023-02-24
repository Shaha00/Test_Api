# Generated by Django 4.1.5 on 2023-02-24 11:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0009_alter_record_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
