# Generated by Django 2.2 on 2019-04-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190428_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topheadline',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]