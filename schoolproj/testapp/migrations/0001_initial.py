# Generated by Django 3.0.7 on 2020-07-05 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('pname', models.CharField(max_length=20)),
                ('DOB', models.DateTimeField()),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=12)),
                ('admno', models.IntegerField()),
                ('classx', models.IntegerField()),
                ('section', models.CharField(max_length=3)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
