# Generated by Django 2.2.5 on 2021-08-07 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Criminology_App', '0002_auto_20210807_0201'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=440)),
                ('event_file', models.FileField(upload_to='Publication')),
            ],
        ),
    ]