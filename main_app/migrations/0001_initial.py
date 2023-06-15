# Generated by Django 4.2.1 on 2023-06-06 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('id_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('id_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('id_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('phone_number', models.CharField(default='', max_length=50)),
                ('id_status', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('id_status', models.BooleanField(default=True)),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_status', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('id_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100)),
                ('aditional_address', models.CharField(max_length=50)),
                ('id_status', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('id_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.city')),
                ('id_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('index', models.IntegerField(default=0)),
                ('id_status', models.BooleanField(default=True)),
                ('id_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.country')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='id_department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.department'),
        ),
    ]
