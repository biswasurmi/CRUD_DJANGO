# Generated by Django 5.1.5 on 2025-02-01 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='course',
            field=models.TextField(default='Unknown'),
        ),
    ]
