# Generated by Django 4.2.1 on 2023-06-15 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_clientmessages'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]
