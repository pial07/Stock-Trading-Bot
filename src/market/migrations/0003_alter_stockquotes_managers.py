# Generated by Django 5.1.8 on 2025-04-20 09:57

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_stockquotes'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='stockquotes',
            managers=[
                ('timescale', django.db.models.manager.Manager()),
            ],
        ),
    ]
