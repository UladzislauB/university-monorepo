# Generated by Django 2.2 on 2019-06-03 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_remove_topheadline_is_fan'),
    ]

    operations = [
        migrations.AddField(
            model_name='topheadline',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
