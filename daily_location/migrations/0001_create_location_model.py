# Generated by Django 4.2.3 on 2023-07-15 08:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
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
                ("domain", models.CharField(max_length=100)),
                ("company_name", models.CharField(max_length=100)),
                ("tiktok_link", models.URLField(max_length=500)),
                ("famous", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                "db_table": "locations",
            },
        ),
    ]
