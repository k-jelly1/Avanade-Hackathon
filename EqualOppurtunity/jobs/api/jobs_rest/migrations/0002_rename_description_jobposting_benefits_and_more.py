# Generated by Django 4.1.7 on 2023-03-06 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_rest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobposting',
            old_name='description',
            new_name='benefits',
        ),
        migrations.RenameField(
            model_name='jobposting',
            old_name='preferred_experience',
            new_name='good_to_have',
        ),
        migrations.RenameField(
            model_name='jobposting',
            old_name='short_description',
            new_name='job_overview',
        ),
        migrations.AddField(
            model_name='jobposting',
            name='requirments',
            field=models.TextField(default='dummydata'),
            preserve_default=False,
        ),
    ]
