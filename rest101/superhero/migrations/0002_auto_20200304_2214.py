# Generated by Django 3.0.3 on 2020-03-05 03:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('superhero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='id',
            field=models.UUIDField(default=uuid.UUID('452162a4-bf4a-4b62-aa04-2ecfa6d4e1bd'), editable=False, primary_key=True, serialize=False),
        ),
    ]
