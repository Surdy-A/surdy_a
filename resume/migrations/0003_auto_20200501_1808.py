# Generated by Django 2.0.12 on 2020-05-01 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20200501_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='percent',
            name='percent',
            field=models.CharField(max_length=100),
        ),
    ]
