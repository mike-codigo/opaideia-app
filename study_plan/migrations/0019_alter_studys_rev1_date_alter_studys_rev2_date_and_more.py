# Generated by Django 4.1 on 2022-09-13 20:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_plan', '0018_alter_courses_certificate_alter_courses_hard_skills_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studys',
            name='rev1_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 14, 20, 7, 9, 152999, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev2_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 20, 20, 7, 9, 152999, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev3_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 13, 20, 7, 9, 152999, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev4_date',
            field=models.DateField(default=datetime.datetime(2022, 11, 12, 20, 7, 9, 152999, tzinfo=datetime.timezone.utc)),
        ),
    ]