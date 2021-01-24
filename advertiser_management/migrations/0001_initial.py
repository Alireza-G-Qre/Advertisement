# Generated by Django 3.1.5 on 2021-01-24 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('clicks', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Advertiser',
            },
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('clicks', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=30)),
                ('link', models.URLField(max_length=2000)),
                ('image_url', models.URLField(max_length=2000)),
                ('description', models.TextField()),
                ('advertiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='advertiser_management.advertiser')),
            ],
            options={
                'verbose_name': 'Advertise',
            },
        ),
    ]
