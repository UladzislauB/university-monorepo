# Generated by Django 2.2 on 2019-05-01 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190428_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topheadline',
            name='likes',
        ),
    ]
