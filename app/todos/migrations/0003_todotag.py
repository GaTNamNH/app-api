# Generated by Django 2.1.5 on 2019-05-03 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20190503_0657'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='todos.Tag')),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='todos.Todo')),
            ],
        ),
    ]
