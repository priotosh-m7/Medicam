# Generated by Django 4.1.2 on 2022-12-29 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analyzers', '0002_alter_uploadimage_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='user',
            field=models.CharField(default=1672319530, max_length=200, verbose_name='username'),
        ),
    ]