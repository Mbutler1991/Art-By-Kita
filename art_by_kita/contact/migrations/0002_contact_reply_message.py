# Generated by Django 5.1.1 on 2024-09-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='reply_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]