# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-14 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='learn_times',
            field=models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u65f6\u957f\uff08\u5206\u949f)'),
        ),
    ]
