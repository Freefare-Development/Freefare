# Generated by Django 3.0.5 on 2020-08-21 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20200820_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpost',
            name='post_image',
        ),
    ]