# Generated by Django 4.0.4 on 2022-07-26 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_plan', '0004_alter_studys_rev1_date_alter_studys_rev2_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('Study', 'Study'), ('Review', 'Review')], default='Study', max_length=6),
        ),
    ]
