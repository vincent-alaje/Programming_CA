# Generated by Django 3.1.7 on 2021-04-19 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Digital_Diary_app', '0004_auto_20210419_1103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
