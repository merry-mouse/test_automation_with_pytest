# Generated by Django 5.0.3 on 2024-03-04 10:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=30, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Layoffs", "Layoffs"),
                            ("Hiring Freeze", "Hiring Freeze"),
                            ("Hiring", "Hiring"),
                        ],
                        default="Hiring",
                        max_length=30,
                    ),
                ),
                (
                    "last_update",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("notes", models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]