# Generated by Django 3.1.13 on 2022-12-11 20:36

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_auto_20220109_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='profile_pics', validators=[main.validators.validate_is_pic], verbose_name='Profile Image'),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='post_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='post_pics', validators=[main.validators.validate_is_pic], verbose_name='Post Image'),
        ),
    ]