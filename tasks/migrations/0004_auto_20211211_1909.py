# Generated by Django 3.2.6 on 2021-12-11 22:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_auto_20211211_1818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='block',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='block',
            name='link',
            field=models.ManyToManyField(related_name='links', to=settings.AUTH_USER_MODEL),
        ),
    ]
