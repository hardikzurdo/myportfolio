# Generated by Django 2.2 on 2019-04-08 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_job_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
