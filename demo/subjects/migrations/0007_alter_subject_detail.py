# Generated by Django 4.1.1 on 2022-09-17 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subjects", "0006_subject_detail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subject",
            name="detail",
            field=models.CharField(default="", max_length=99999),
        ),
    ]
