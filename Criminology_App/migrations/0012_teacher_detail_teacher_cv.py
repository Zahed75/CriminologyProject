# Generated by Django 2.2.5 on 2021-07-15 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Criminology_App', '0011_remove_research_publication_feature_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_detail',
            name='teacher_cv',
            field=models.FileField(default=1, upload_to='Cv'),
            preserve_default=False,
        ),
    ]
