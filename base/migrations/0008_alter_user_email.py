# Generated by Django 5.0.3 on 2024-03-28 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_user_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
