# Generated by Django 4.1.1 on 2022-09-10 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_remove_subject_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
