# Generated by Django 3.0.3 on 2020-03-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superhero', '0004_auto_20200305_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
