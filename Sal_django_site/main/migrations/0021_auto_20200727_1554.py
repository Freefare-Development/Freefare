# Generated by Django 3.0.5 on 2020-07-27 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20200727_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='org_zipcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
