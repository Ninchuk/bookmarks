# Generated by Django 4.1.7 on 2023-03-22 06:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),  # noqa: BLK100
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actions',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('verd', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('target_id', models.PositiveIntegerField(blank=True, null=True)),
                (
                    'target_ct',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='target_obj',
                        to='contenttypes.contenttype',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='actions',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddIndex(
            model_name='actions',
            index=models.Index(
                fields=['-created'], name='actions_act_created_639f69_idx'
            ),
        ),
        migrations.AddIndex(
            model_name='actions',
            index=models.Index(
                fields=['target_ct', 'target_id'], name='actions_act_target__5ecc2e_idx'
            ),
        ),
    ]