# Generated by Django 3.2.20 on 2023-08-24 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_comment_surname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approved_by',
            new_name='approved',
        ),
    ]