# Generated by Django 2.2.5 on 2021-07-14 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Criminology_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilite',
            name='facilites_title',
            field=models.TextField(max_length=700, verbose_name='Put your facilites title here'),
        ),
        migrations.AlterField(
            model_name='facilites_details',
            name='details',
            field=models.TextField(max_length=3000, verbose_name='Put here facilites details'),
        ),
    ]
