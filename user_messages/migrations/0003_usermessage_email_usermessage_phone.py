# Generated by Django 5.1.1 on 2024-10-10 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_messages', '0002_usermessage_delete_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
