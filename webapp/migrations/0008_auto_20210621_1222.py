# Generated by Django 3.2.2 on 2021-06-21 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20210612_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='slug',
        ),
    ]
