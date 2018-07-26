# Generated by Django 2.0.7 on 2018-07-17 17:38

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0002_auto_20180717_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexternaltool',
            name='user',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
