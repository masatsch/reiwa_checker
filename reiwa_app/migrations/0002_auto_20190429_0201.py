# Generated by Django 2.2 on 2019-04-29 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reiwa_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
    ]