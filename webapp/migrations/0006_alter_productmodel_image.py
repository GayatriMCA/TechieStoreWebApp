# Generated by Django 3.2.2 on 2021-06-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_productmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(upload_to='products/images'),
        ),
    ]
