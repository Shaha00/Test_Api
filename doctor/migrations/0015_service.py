# Generated by Django 4.1.7 on 2023-03-17 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("doctor", "0014_alter_doctor_education_alter_doctor_post"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "names",
                    models.CharField(
                        max_length=50, null=True, verbose_name="Названия отделов"
                    ),
                ),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="doctor.doctor",
                        verbose_name="Врач",
                    ),
                ),
            ],
            options={
                "verbose_name": "Информация об Услугах",
                "verbose_name_plural": "Добавить Услугу",
            },
        ),
    ]
