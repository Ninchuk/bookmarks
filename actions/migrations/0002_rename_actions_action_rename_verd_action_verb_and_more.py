# Generated by Django 4.1.7 on 2023-03-22 06:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actions',
            new_name='Action',
        ),
        migrations.RenameField(
            model_name='action',
            old_name='verd',
            new_name='verb',
        ),
        migrations.RenameIndex(
            model_name='action',
            new_name='actions_act_created_64f10d_idx',
            old_name='actions_act_created_639f69_idx',
        ),
        migrations.RenameIndex(
            model_name='action',
            new_name='actions_act_target__f20513_idx',
            old_name='actions_act_target__5ecc2e_idx',
        ),
    ]