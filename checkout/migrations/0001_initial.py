# Generated by Django 3.2 on 2022-01-14 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=16)),
                ('full_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=255)),
                ('user_trainer_code', models.CharField(max_length=255)),
                ('total_requests', models.IntegerField(default=0, max_length=16)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                            related_name='lineitems',
                                            to='checkout.order')),
            ],
        ),
    ]
