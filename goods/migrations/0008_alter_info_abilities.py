# Generated by Django 3.2 on 2022-01-15 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_auto_20220115_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='abilities',
            field=models.CharField(max_length=100),
        ),
    ]