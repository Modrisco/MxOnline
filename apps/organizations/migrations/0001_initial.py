# Generated by Django 2.2 on 2019-12-30 06:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add time')),
                ('name', models.CharField(max_length=50, verbose_name='city name')),
                ('desc', models.TextField(verbose_name='city description')),
            ],
            options={
                'verbose_name': 'city organization',
                'verbose_name_plural': 'city organization',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add time')),
                ('name', models.CharField(max_length=50, verbose_name='org name')),
                ('desc', models.TextField(verbose_name='org description')),
                ('tag', models.CharField(default='World', max_length=10, verbose_name='org tag')),
                ('category', models.CharField(choices=[('tafe', 'tafe'), ('uni', 'university'), ('indi', 'individual')], max_length=4, verbose_name='org category')),
                ('click_nums', models.IntegerField(default=0, verbose_name='number of clicks')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='number of favorites')),
                ('logo', models.ImageField(upload_to='org/%Y/%m', verbose_name='org logo')),
                ('address', models.CharField(max_length=150, verbose_name='org address')),
                ('students', models.IntegerField(default=0, verbose_name='number of students')),
                ('course_nums', models.IntegerField(default=0, verbose_name='number of courses')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.City', verbose_name='city located')),
            ],
            options={
                'verbose_name': 'course organization',
                'verbose_name_plural': 'course organization',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add time')),
                ('name', models.CharField(max_length=50, verbose_name='teacher name')),
                ('work_years', models.IntegerField(default=0, verbose_name='work years')),
                ('work_company', models.CharField(max_length=50, verbose_name='work company')),
                ('work_position', models.CharField(max_length=50, verbose_name='work position')),
                ('characteristics', models.CharField(max_length=50, verbose_name='teaching characteristics')),
                ('click_nums', models.IntegerField(default=0, verbose_name='number of clicks')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='number of favorites')),
                ('age', models.IntegerField(default=18, verbose_name='teacher age')),
                ('avatar', models.ImageField(upload_to='teacher/%Y/%m', verbose_name='teacher avatar')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.CourseOrg', verbose_name='teacher org')),
            ],
            options={
                'verbose_name': 'course lecturer',
                'verbose_name_plural': 'course lecturer',
            },
        ),
    ]