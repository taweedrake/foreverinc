# Generated by Django 4.1.3 on 2022-12-06 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile_delete_useraccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='hide_email',
            field=models.BooleanField(default=False),
        ),
    ]