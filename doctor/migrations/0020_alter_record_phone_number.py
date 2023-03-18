# Generated by Django 4.1.7 on 2023-03-18 15:05

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("doctor", "0019_doctor_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                default="+996",
                max_length=13,
                region=None,
                verbose_name="Номер телефона",
            ),
        ),
    ]