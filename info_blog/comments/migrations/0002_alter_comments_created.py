# Generated by Django 4.0 on 2021-12-17 02:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
