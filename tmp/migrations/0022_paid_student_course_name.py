# Generated by Django 3.2.16 on 2022-12-24 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmp', '0021_auto_20221224_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='paid_student',
            name='course_name',
            field=models.CharField(default='kps', max_length=150),
            preserve_default=False,
        ),
    ]
