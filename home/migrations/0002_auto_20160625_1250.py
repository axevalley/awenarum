# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 11:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomepageArticles',
            new_name='HomepageArticle',
        ),
    ]
