# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0003_auto_20161025_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('join', models.ManyToManyField(related_name='joined_user', to='user_app.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mywishlist', to='user_app.User')),
            ],
        ),
    ]
