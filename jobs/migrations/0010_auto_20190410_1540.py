# Generated by Django 2.2 on 2019-04-10 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20190409_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.TextField(max_length=500),
        ),
    ]
