# Generated by Django 3.0.8 on 2020-07-30 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20200730_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='countries',
        ),
    ]