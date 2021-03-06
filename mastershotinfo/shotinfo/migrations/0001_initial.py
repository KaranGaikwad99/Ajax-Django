# Generated by Django 2.1.4 on 2018-12-26 09:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shotinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shot_type', models.CharField(blank=True, max_length=255, null=True)),
                ('shot_status', models.CharField(blank=True, max_length=255, null=True)),
                ('shot_record', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('timestamp_added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'ShotInfo',
            },
        ),
    ]
