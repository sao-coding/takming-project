# Generated by Django 4.1.3 on 2022-11-09 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import randomslugfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Member_info",
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
                ("room", models.PositiveIntegerField()),
                ("bed", models.SlugField(max_length=10)),
                ("member_class", models.CharField(max_length=5)),
                ("student_ID", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=5)),
                ("ID_number", models.CharField(max_length=10)),
                ("birthday", models.DateField()),
                ("phone", models.CharField(max_length=10)),
                ("home_phone", models.CharField(max_length=10)),
                ("address", models.CharField(max_length=200)),
                ("emergency_contact", models.CharField(max_length=10)),
                ("emergency_contact_phone", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("about", models.TextField(blank=True, max_length=500)),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("??????", "??????"),
                            ("??????", "??????"),
                            ("??????", "??????"),
                            ("??????", "??????"),
                        ],
                        default="??????",
                        max_length=4,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                    "slug",
                    randomslugfield.fields.RandomSlugField(
                        blank=True, editable=False, length=7, max_length=7, unique=True
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
