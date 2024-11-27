# Generated by Django 5.1.3 on 2024-11-27 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TempEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(default='943df935@tempmail.com', max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('sender', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('received_at', models.DateTimeField(auto_now_add=True)),
                ('temp_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='emailapp.tempemail')),
            ],
        ),
    ]
