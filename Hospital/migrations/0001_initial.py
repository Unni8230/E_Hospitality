# Generated by Django 5.2.2 on 2025-06-10 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Unknown', max_length=100, unique=True)),
                ('name', models.CharField(default='Unknown', max_length=255)),
                ('email', models.EmailField(default='Unknown', max_length=255, unique=True)),
                ('phone', models.CharField(default='Unknown', max_length=12)),
                ('password', models.CharField(default='Unknown', max_length=255)),
                ('type', models.CharField(default='Unknown', max_length=50)),
            ],
        ),
    ]
