# Generated by Django 3.2.2 on 2021-06-10 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20210609_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorymodel',
            old_name='brand',
            new_name='name',
        ),
    ]