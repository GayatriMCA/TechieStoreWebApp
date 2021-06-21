# Generated by Django 3.2.2 on 2021-06-09 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_categorymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.categorymodel'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='slug',
            field=models.SlugField(default=True, max_length=200),
        ),
    ]