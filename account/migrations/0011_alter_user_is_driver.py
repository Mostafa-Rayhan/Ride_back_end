# Generated by Django 3.2.9 on 2021-12-25 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_remove_help_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_driver',
            field=models.BooleanField(default=False, verbose_name='Is driver'),
        ),
    ]
