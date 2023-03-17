# Generated by Django 4.1.7 on 2023-03-17 14:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctor", "0012_alter_record_phone_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doctor",
            name="surname",
        ),
        migrations.AddField(
            model_name="doctor",
            name="education",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Образование"
            ),
        ),
        migrations.AddField(
            model_name="doctor",
            name="post",
            field=models.TextField(null=True, verbose_name="Должность"),
        ),
    ]
