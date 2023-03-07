# Generated by Django 4.1 on 2022-09-14 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_plan', '0024_alter_courses_certificate_alter_studys_rev1_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='notes',
            field=models.TextField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='transcript',
            field=models.TextField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev1_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 15, 12, 58, 32, 654199, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev2_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 21, 12, 58, 32, 654199, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev3_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 14, 12, 58, 32, 654199, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev4_date',
            field=models.DateField(default=datetime.datetime(2022, 11, 13, 12, 58, 32, 654199, tzinfo=datetime.timezone.utc)),
        ),
    ]