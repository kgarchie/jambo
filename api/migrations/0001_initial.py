# Generated by Django 5.0.4 on 2024-04-28 01:16

import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Business Categories',
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Counties',
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ulid', models.CharField(max_length=26, unique=True, verbose_name='ULID')),
                ('business_name', models.CharField(max_length=255, verbose_name='Business Name')),
                ('business_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number')),
                ('business_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('business_address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('business_website', models.CharField(blank=True, max_length=255, null=True, verbose_name='Website')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.businesscategory')),
            ],
            options={
                'verbose_name_plural': 'Businesses',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ulid', models.CharField(max_length=26, unique=True, verbose_name='ULID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('middle_name', models.CharField(blank=True, max_length=255, verbose_name='Middle Name')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('nationality', django_countries.fields.CountryField(max_length=2, verbose_name='Nationality')),
                ('phone_number', models.CharField(max_length=20, unique=True, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('businesses', models.ManyToManyField(related_name='customers', to='api.business')),
            ],
        ),
        migrations.CreateModel(
            name='SubCounty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.county')),
            ],
            options={
                'verbose_name_plural': 'Sub Counties',
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('customer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('sub_county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subcounty')),
            ],
            options={
                'verbose_name_plural': 'Wards',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ward')),
            ],
            options={
                'verbose_name_plural': 'Areas',
            },
        ),
    ]
