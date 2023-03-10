# Generated by Django 4.1 on 2022-09-12 15:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('study_plan', '0016_alter_studys_rev1_date_alter_studys_rev2_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructors',
            name='name',
        ),
        migrations.AddField(
            model_name='instructors',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='instructor_courses', to='study_plan.courses'),
        ),
        migrations.RemoveField(
            model_name='certificates',
            name='course',
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev1_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 13, 15, 14, 10, 826453, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev2_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 19, 15, 14, 10, 826453, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev3_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 12, 15, 14, 10, 826453, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='studys',
            name='rev4_date',
            field=models.DateField(default=datetime.datetime(2022, 11, 11, 15, 14, 10, 826453, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.ManyToManyField(blank=True, related_name='student_courses', to='study_plan.courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_students', models.IntegerField()),
                ('course_days', multiselectfield.db.fields.MultiSelectField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=15)),
                ('course_schedule', models.TimeField()),
                ('duration', models.CharField(choices=[('1 hour', '1 hour'), ('1:30 hour', '1:30 hour'), ('2 hours', '2 hours'), ('2:30 hours', '2:30 hours'), ('3 hours', '3 hours')], max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms_course', to='study_plan.courses')),
                ('students', models.ManyToManyField(related_name='rooms_students', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='rooms',
            field=models.ManyToManyField(related_name='course_rooms', to='study_plan.rooms'),
        ),
        migrations.AddField(
            model_name='certificates',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='certificate_course', to='study_plan.courses'),
        ),
    ]
