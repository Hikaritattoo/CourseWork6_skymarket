# Generated by Django 4.1.1 on 2022-10-04 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("admin", "admin"), ("user", "user")],
                default="user",
                max_length=5,
                null=True,
            ),
        ),
    ]
