# Generated by Django 5.0.4 on 2024-04-27 13:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_business_ulid'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 4, 27, 13, 10, 30, 551196, tzinfo=datetime.timezone.utc), verbose_name='Created At'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='business',
            name='ulid',
            field=models.CharField(default='01HWFTTS3R9ZAVJ9D4KRG8720M', max_length=26, unique=True, verbose_name='ULID'),
        ),
    ]
