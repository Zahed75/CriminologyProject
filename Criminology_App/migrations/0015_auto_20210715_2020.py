# Generated by Django 2.2.5 on 2021-07-15 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Criminology_App', '0014_computer_lab'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computer_lab',
            old_name='seminar_details',
            new_name='lab_details',
        ),
        migrations.RenameField(
            model_name='computer_lab',
            old_name='seminar_image',
            new_name='lab_image',
        ),
    ]
