# Generated by Django 4.1.7 on 2023-03-22 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("name", models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Movements",
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
                ("date", models.DateField(auto_now=True)),
                (
                    "type",
                    models.TextField(
                        choices=[("PAGO", "Pago"), ("INGRESO", "Ingreso")]
                    ),
                ),
                ("description", models.TextField(max_length=128)),
                ("quantity", models.PositiveIntegerField()),
                ("amount", models.FloatField()),
                (
                    "client",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_client.client",
                    ),
                ),
            ],
        ),
    ]
