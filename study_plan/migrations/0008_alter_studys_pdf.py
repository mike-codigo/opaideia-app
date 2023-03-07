# Generated by Django 4.1 on 2022-09-09 16:49

from django.db import migrations, models
import study_plan.models


class Migration(migrations.Migration):

    dependencies = [
        ('study_plan', '0007_studys_pdf_alter_studys_rev1_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studys',
            name='pdf',
            field=models.FileField(default=None, upload_to=study_plan.models.get_upload_path),
        ),
    ]
