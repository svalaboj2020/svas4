# Generated by Django 3.0.7 on 2020-07-21 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0024_auto_20200721_2112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rv_upload',
            old_name='mp4',
            new_name='pdf',
        ),
    ]
