# Generated by Django 4.1.5 on 2023-02-08 19:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study_plan', '0047_alter_studys_rev1_date_alter_studys_rev2_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studys',
            name='user_create',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev1_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 9, 19, 28, 10, 145235, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev2_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 19, 28, 10, 145235, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev3_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 10, 19, 28, 10, 145235, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev4_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 9, 19, 28, 10, 145235, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='summary',
            field=models.CharField(max_length=1500),
        ),
    ]
