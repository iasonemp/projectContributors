# Generated by Django 5.0.1 on 2024-01-20 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.PositiveIntegerField()),
                ('country', models.CharField(max_length=100)),
                ('residence', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
