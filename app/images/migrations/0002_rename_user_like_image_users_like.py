# Generated by Django 4.1.7 on 2023-03-21 07:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('images', '0001_initial'),  # noqa: BLK100
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='user_like',
            new_name='users_like',
        ),
    ]