# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-26 05:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0010_remove_student_graduate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Swaphelper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='fee_receipt',
            field=models.FileField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='swaphelper',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel.Student'),
        ),
    ]
