# Generated by Django 5.0.3 on 2024-03-16 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='id',
        ),
    ]