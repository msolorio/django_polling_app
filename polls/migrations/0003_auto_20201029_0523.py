# Generated by Django 3.1.2 on 2020-10-29 05:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20201028_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 29, 5, 23, 55, 260028, tzinfo=utc), verbose_name='date published'),
        ),
    ]
