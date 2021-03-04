# Generated by Django 3.1.7 on 2021-03-02 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_auto_20210302_1933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizations',
            options={'verbose_name': 'Organization', 'verbose_name_plural': 'Organizations'},
        ),
        migrations.AddField(
            model_name='organizations',
            name='OrgID',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizations',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organizations',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterModelTable(
            name='organizations',
            table='Organizations_tb',
        ),
    ]
