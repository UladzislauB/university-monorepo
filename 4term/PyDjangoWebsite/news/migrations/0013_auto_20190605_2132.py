# Generated by Django 2.2 on 2019-06-05 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20190605_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='topheadline',
            name='is_true',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='topheadline',
            name='is_true_prob',
            field=models.FloatField(default=0),
        ),
    ]
