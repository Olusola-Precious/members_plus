# Generated by Django 3.1.7 on 2021-03-03 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0005_auto_20210302_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='role',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Admin', 'admin')], max_length=50),
        ),
    ]
