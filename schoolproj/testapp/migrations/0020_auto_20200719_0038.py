# Generated by Django 3.0.7 on 2020-07-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0019_auto_20200717_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='SM_upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('subject', models.CharField(max_length=20)),
                ('std', models.IntegerField()),
                ('sec', models.CharField(max_length=1)),
                ('pdf', models.FileField(blank=True, upload_to='books/pdfs')),
            ],
        ),
        migrations.DeleteModel(
            name='Assignment_upload',
        ),
    ]
