# Generated by Django 2.1.5 on 2019-06-04 02:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0002_load_fixture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cover', models.ImageField(default='images.png', upload_to='media')),
                ('body', models.TextField()),
                ('intro', models.CharField(max_length=500)),
                ('state', models.IntegerField(choices=[(-1, 'Draft'), (0, 'Not published'), (1, 'Published')], default=-1)),
                ('publish_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(blank=True, to='posts.Category')),
                ('majors', models.ManyToManyField(blank=True, to='job.Major')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish_time'],
            },
        ),
    ]
