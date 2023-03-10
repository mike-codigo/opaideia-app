# Generated by Django 4.1 on 2022-09-09 16:52

from django.db import migrations, models
import study_plan.models


class Migration(migrations.Migration):

    dependencies = [
        ('study_plan', '0008_alter_studys_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studys',
            name='pdf',
            field=models.FileField(blank=True, default='', upload_to=study_plan.models.get_upload_path),
        ),
        migrations.AlterField(
            model_name='studys',
            name='teaching_audio',
            field=models.FileField(blank=True, default='', upload_to=study_plan.models.get_upload_path),
        ),
    ]
