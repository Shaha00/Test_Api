# Generated by Django 4.1.7 on 2023-02-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_review_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(verbose_name='Назначить Дату и Время Приема'),
        ),
    ]
