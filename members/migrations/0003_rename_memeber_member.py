# Generated by Django 5.0.1 on 2024-01-29 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_rename_memebers_memeber'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Memeber',
            new_name='Member',
        ),
    ]
