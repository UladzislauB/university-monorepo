# Generated by Django 2.2 on 2019-06-05 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_topheadline_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='topheadline',
            name='is_true',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topheadline',
            name='is_true_prob',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
