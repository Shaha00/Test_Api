# Generated by Django 4.1.7 on 2023-03-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctor", "0018_alter_service_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="image",
            field=models.ImageField(
                default="photo_2023-03-18_20-43-19.jpg", upload_to=""
            ),
        ),
    ]
