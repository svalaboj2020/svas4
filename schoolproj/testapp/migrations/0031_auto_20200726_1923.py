# Generated by Django 3.0.7 on 2020-07-26 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0030_rlink_upload_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment_submission',
            name='assignment',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignment', to='testapp.Assignment'),
        ),
    ]
