# Generated by Django 4.1.2 on 2023-01-04 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analyzers', '0009_alter_uploadchestimage_user_alter_uploadimage_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadchestimage',
            name='user',
            field=models.CharField(default=856385, max_length=200, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='uploadkidneyimage',
            name='user',
            field=models.CharField(default=200131, max_length=200, verbose_name='username'),
        ),
    ]
