# Generated by Django 4.1.5 on 2023-02-09 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_plan', '0049_alter_studys_rev1_date_alter_studys_rev2_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studys',
            name='rev1_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 10, 10, 32, 43, 628989)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev2_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 16, 10, 32, 43, 628989)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev3_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 11, 10, 32, 43, 628989)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev4_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 10, 10, 32, 43, 628989)),
        ),
    ]
