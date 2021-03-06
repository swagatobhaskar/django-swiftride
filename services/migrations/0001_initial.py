# Generated by Django 2.1.5 on 2019-03-06 17:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='images/profile-photos', verbose_name='Upload a profile picture')),
                ('mobile', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
                ('building_no', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=15)),
                ('zip', models.IntegerField()),
                ('country', models.CharField(max_length=20)),
                ('sex', models.CharField(blank=True, max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Car_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('company', models.CharField(max_length=15)),
                ('mileage', models.DecimalField(decimal_places=1, max_digits=4)),
                ('rent_per_hour', models.DecimalField(decimal_places=4, max_digits=6)),
                ('photo', models.ImageField(upload_to='images/models')),
            ],
        ),
        migrations.CreateModel(
            name='Card_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_no', models.IntegerField()),
                ('year_expires', models.DateField()),
                ('cardholder_name', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Driving_license',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_issued_in', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('license_no', models.CharField(max_length=15)),
                ('expiry_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Driving_plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=25)),
                ('duration', models.CharField(max_length=15)),
                ('details1', models.TextField(blank=True)),
                ('details2', models.TextField(blank=True)),
                ('one_time_fee', models.DecimalField(decimal_places=2, default=25.0, max_digits=4)),
                ('hourly_rate', models.DecimalField(decimal_places=2, default=8.0, max_digits=4)),
                ('monthly_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('daily_rate', models.DecimalField(decimal_places=2, default=65.0, max_digits=4)),
                ('annual_fee', models.DecimalField(decimal_places=2, default=50.0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('zip', models.IntegerField(blank=True, null=True)),
                ('area', models.CharField(blank=True, max_length=30)),
                ('street', models.CharField(blank=True, max_length=20)),
                ('pic', models.ImageField(upload_to='images/garages')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('driving_plans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Driving_plan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('time_from', models.TimeField()),
                ('time_to', models.TimeField()),
                ('destination', models.CharField(max_length=20, verbose_name='Where will you go')),
                ('chosen_vehicle', models.CharField(default='', max_length=20)),
                ('booking_time', models.DateTimeField(default=datetime.datetime.now)),
                ('garage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Garage', verbose_name='Start from')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_no', models.CharField(max_length=20)),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Car_model')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Category')),
                ('garage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Garage')),
            ],
        ),
        migrations.AddField(
            model_name='car_model',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Category'),
        ),
    ]
