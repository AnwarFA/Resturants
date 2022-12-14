# Generated by Django 4.1.2 on 2022-10-11 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(default='')),
                ('opening_time', models.IntegerField()),
                ('closing_time', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 11, 18, 14, 8, 847867))),
            ],
        ),
    ]
