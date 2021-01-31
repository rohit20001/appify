# Generated by Django 2.2.5 on 2021-01-31 07:30

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content_upper_para', ckeditor.fields.RichTextField()),
                ('content_lower_para', ckeditor.fields.RichTextField(default='')),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('postedBy', models.CharField(max_length=20)),
                ('blogImage', models.ImageField(default='', upload_to='blog/images')),
                ('authorImage', models.ImageField(default='', upload_to='author/images')),
                ('aboutAuthor', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
