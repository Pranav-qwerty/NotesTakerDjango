# Generated by Django 3.1.3 on 2021-01-14 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='date',
        ),
    ]