# Generated by Django 5.0.4 on 2024-04-27 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_business_ulid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='ulid',
            field=models.CharField(default='01HWFS4JYQRFXJE2005976PJGK', max_length=26, unique=True, verbose_name='ULID'),
        ),
    ]
