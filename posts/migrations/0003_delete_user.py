# Generated by Django 2.1.3 on 2018-11-27 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_user_is_admin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
