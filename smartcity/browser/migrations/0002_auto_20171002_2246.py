# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-02 12:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hotels',
            new_name='Hotel',
        ),
    ]