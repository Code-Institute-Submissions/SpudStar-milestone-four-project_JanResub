# Generated by Django 3.2.9 on 2021-11-29 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20211129_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='pdex_no',
            field=models.IntegerField(default=1),
        ),
    ]