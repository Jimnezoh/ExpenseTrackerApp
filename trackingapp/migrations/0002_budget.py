# Generated by Django 4.2.7 on 2023-11-28 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackingapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('Amount', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
    ]
