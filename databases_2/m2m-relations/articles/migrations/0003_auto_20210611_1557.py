# Generated by Django 3.1.2 on 2021-06-11 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210611_0254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlesection',
            old_name='section',
            new_name='sections',
        ),
    ]