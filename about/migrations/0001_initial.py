# Generated by Django 2.0.12 on 2020-04-18 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('blood', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=254)),
                ('about', models.CharField(max_length=500)),
                ('image', models.FileField(upload_to='images/')),
            ],
        ),
    ]
