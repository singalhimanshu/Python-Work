# Generated by Django 2.2.1 on 2019-05-25 03:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190525_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 25, 3, 34, 28, 960733), verbose_name='date published'),
        ),
    ]
