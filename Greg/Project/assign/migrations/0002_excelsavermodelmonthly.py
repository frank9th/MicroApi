# Generated by Django 3.0.7 on 2020-06-27 13:51

import assign.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelSaverModelMonthly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthly_file', models.FileField(null=True, upload_to=assign.models.monthly_file_handler)),
            ],
        ),
    ]
