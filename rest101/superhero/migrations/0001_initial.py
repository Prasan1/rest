# Generated by Django 3.0.3 on 2020-03-05 03:07

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('squadName', models.CharField(max_length=50)),
                ('hometown', models.CharField(max_length=30)),
                ('formed', models.DateField()),
                ('active', models.BooleanField()),
                ('members', django_mysql.models.JSONField(default=dict)),
            ],
            options={
                'db_table': 'superheros',
                'ordering': ('active',),
            },
        ),
    ]