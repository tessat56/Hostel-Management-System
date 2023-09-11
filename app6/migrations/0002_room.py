# Generated by Django 4.2.2 on 2023-08-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app6', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('rent', models.FloatField()),
                ('vacancy', models.PositiveIntegerField()),
            ],
        ),
    ]
