# Generated by Django 3.0.5 on 2020-07-14 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_profile_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='color',
        ),
        migrations.AlterField(
            model_name='profile',
            name='org_role',
            field=models.CharField(choices=[('DONOR', 'Donor'), ('RECIPIENT', 'Recipient'), ('BOTH', 'Both')], default='DONOR', max_length=10),
        ),
    ]
