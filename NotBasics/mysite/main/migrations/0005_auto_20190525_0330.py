# Generated by Django 2.2.1 on 2019-05-25 03:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190525_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 25, 3, 30, 11, 894252), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.TutorialSeries', verbose_name='Series'),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='tutorial_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.TutorialCategory', verbose_name='Category'),
        ),
    ]