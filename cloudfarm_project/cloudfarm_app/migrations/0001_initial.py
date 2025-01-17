# Generated by Django 5.0.6 on 2024-11-19 04:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserRegistration",
            fields=[
                (
                    "number",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("name", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="UserLogin",
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
                ("password", models.CharField(max_length=255)),
                (
                    "number",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cloudfarm_app.userregistration",
                    ),
                ),
            ],
        ),
    ]
