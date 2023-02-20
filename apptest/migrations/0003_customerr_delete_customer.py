# Generated by Django 4.1.4 on 2023-02-20 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("apptest", "0002_customer_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="customerr",
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
                ("card", models.IntegerField()),
                ("country", models.CharField(max_length=100)),
                ("image", models.ImageField(null=True, upload_to="img/customer/")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="customer",
        ),
    ]
