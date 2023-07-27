# Generated by Django 4.2.3 on 2023-07-27 10:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_timingtodo_timing_todo_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timingtodo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('7776693c-dee3-458e-bba6-753c48efd00e'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('7776693c-dee3-458e-bba6-753c48efd00e'), editable=False, primary_key=True, serialize=False),
        ),
    ]
