# Generated by Django 2.2 on 2019-04-04 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_about_contact_education_project_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='extra',
        ),
        migrations.AddField(
            model_name='education',
            name='project',
            field=models.TextField(default='dddd'),
            preserve_default=False,
        ),
    ]