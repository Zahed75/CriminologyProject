# Generated by Django 2.2.5 on 2021-08-06 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Criminology_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.TextField(max_length=400)),
                ('event_file', models.FileField(upload_to='Syllabus')),
            ],
        ),
        migrations.DeleteModel(
            name='New_event',
        ),
    ]