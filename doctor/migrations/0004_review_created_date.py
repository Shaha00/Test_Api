# Generated by Django 4.1.7 on 2023-02-24 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_review_options_remove_review_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
    ]