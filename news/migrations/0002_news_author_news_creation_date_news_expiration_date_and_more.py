# Generated by Django 4.2.3 on 2023-09-02 21:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="author",
            field=models.TextField(default="admin"),
        ),
        migrations.AddField(
            model_name="news",
            name="creation_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="news",
            name="expiration_date",
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="news",
            name="status",
            field=models.CharField(
                choices=[
                    ("ac", "Active"),
                    ("ex", "Expired"),
                    ("in", "Inactive"),
                    ("pr", "Periodic"),
                ],
                default="ac",
                max_length=2,
            ),
        ),
        migrations.AddField(
            model_name="news",
            name="tag",
            field=models.CharField(
                choices=[("ur", "Urgent"), ("lp", "Low_priority"), ("tr", "Trending")],
                default="",
                max_length=2,
            ),
        ),
        migrations.AddField(
            model_name="news",
            name="text",
            field=models.TextField(default="text"),
        ),
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.CharField(default="title", max_length=300),
        ),
    ]
