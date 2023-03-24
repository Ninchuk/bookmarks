# Generated by Django 4.1.7 on 2023-03-20 13:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',  # noqa: BLK100
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
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('url', models.URLField(max_length=2000)),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('created', models.DateField(auto_now_add=True)),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='images_created',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    'user_like',
                    models.ManyToManyField(
                        blank=True,
                        related_name='images_liked',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(
                fields=['-created'], name='images_imag_created_d57897_idx'
            ),
        ),
    ]
