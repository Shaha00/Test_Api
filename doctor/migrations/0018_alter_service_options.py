# Generated by Django 4.1.7 on 2023-03-17 15:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("doctor", "0017_alter_service_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="service",
            options={"verbose_name": "Услуга", "verbose_name_plural": "Услуги"},
        ),
    ]