# Generated by Django 4.1.7 on 2023-03-02 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receipts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipt",
            name="date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
