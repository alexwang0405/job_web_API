# Generated by Django 4.1.4 on 2023-01-02 12:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_alter_job_web'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
