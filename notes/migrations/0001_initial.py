# Generated by Django 4.2.3 on 2023-07-26 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Note Title')),
                ('content', models.CharField(max_length=10000, verbose_name='Note Content')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('short_title', models.CharField(max_length=12, verbose_name='Note Slug')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
