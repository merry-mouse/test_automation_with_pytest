# Generated by Django 5.0.3 on 2024-03-04 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="application_link",
            field=models.URLField(default=""),
        ),
    ]
