# Generated by Django 3.2.16 on 2022-12-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmp', '0015_rename_paid_students_paid_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='paid_student',
            name='course_name',
            field=models.EmailField(default='coding', max_length=150),
            preserve_default=False,
        ),
    ]