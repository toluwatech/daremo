# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-28 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niji', '0003_forumavatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumavatar',
            name='image',
            field=models.ImageField(blank=True, default='', max_length=255, null=True, upload_to='uploads/forum/avatars/'),
        ),
    ]