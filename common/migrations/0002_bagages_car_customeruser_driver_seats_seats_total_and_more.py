# Generated by Django 4.2.10 on 2024-02-18 16:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bagages",
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
            ],
        ),
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "car_number",
                    models.CharField(
                        max_length=30, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("bagages", models.ManyToManyField(to="common.bagages")),
            ],
        ),
        migrations.CreateModel(
            name="CustomerUser",
            fields=[
                (
                    "first_phone_number",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                ("second_phone_number", models.IntegerField(default=0)),
                ("customer_name", models.CharField(max_length=150)),
                ("cin", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Driver",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=250)),
                ("phone_number", models.IntegerField(default=0)),
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
        migrations.AddField(
            model_name="seats",
            name="seats_total",
            field=models.IntegerField(default=32),
        ),
        migrations.AddField(
            model_name="seats",
            name="seats_used",
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name="Customer",
        ),
        migrations.AddField(
            model_name="customeruser",
            name="seats",
            field=models.ManyToManyField(to="common.seats"),
        ),
        migrations.AddField(
            model_name="car",
            name="customer",
            field=models.ManyToManyField(to="common.customeruser"),
        ),
        migrations.AddField(
            model_name="car",
            name="destination",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="common.destination",
            ),
        ),
        migrations.AddField(
            model_name="car",
            name="driver",
            field=models.ManyToManyField(to="common.driver"),
        ),
        migrations.AddField(
            model_name="car",
            name="seats",
            field=models.ManyToManyField(to="common.seats"),
        ),
    ]
