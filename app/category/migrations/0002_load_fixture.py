# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.core.management import call_command


def load_category_initial_data(apps, schema_editor):
    call_command("loaddata", "category.json")


class Migration(migrations.Migration):
    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_category_initial_data),
    ]