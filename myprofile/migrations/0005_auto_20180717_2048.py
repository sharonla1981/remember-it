# Generated by Django 2.0.7 on 2018-07-17 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0004_userexternaltool_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexternaltool',
            name='user_token',
            field=models.CharField(max_length=500, null=True),
        ),
    ]