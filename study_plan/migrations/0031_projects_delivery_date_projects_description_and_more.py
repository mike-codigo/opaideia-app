# Generated by Django 4.1 on 2022-09-14 15:40

import datetime
from django.db import migrations, models
import study_plan.models


class Migration(migrations.Migration):

    dependencies = [
        ('study_plan', '0030_alter_studys_rev1_date_alter_studys_rev2_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='delivery_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='description',
            field=models.TextField(default='', max_length=100000),
        ),
        migrations.AddField(
            model_name='projects',
            name='hints',
            field=models.TextField(default='', max_length=100000),
        ),
        migrations.AddField(
            model_name='projects',
            name='how_to_send',
            field=models.TextField(default='', max_length=100000),
        ),
        migrations.AddField(
            model_name='projects',
            name='specifications',
            field=models.TextField(default='', max_length=100000),
        ),
        migrations.AddField(
            model_name='projects',
            name='start_file',
            field=models.FileField(blank=True, max_length=500, upload_to=study_plan.models.get_upload_path_projects),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='projects',
            field=models.ManyToManyField(blank=True, default='', related_name='lesson_project', to='study_plan.projects'),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev1_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 15, 12, 40, 49, 465746)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev2_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 21, 12, 40, 49, 465746)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev3_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 14, 12, 40, 49, 465746)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev4_date',
            field=models.DateField(default=datetime.datetime(2022, 11, 13, 12, 40, 49, 465746)),
        ),
    ]