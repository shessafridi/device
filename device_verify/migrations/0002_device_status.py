# Generated by Django 2.2.4 on 2019-09-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_verify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
