# Generated by Django 3.2.9 on 2021-12-02 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_employee',
        ),
        migrations.AddField(
            model_name='user',
            name='is_driver',
            field=models.BooleanField(default=False, verbose_name='Is drier'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_rider',
            field=models.BooleanField(default=False, verbose_name='Is rider'),
        ),
    ]