# Generated by Django 2.0.7 on 2018-07-21 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0009_auto_20180721_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userexternaltool',
            old_name='user_token',
            new_name='user_access_info',
        ),
    ]
