# Generated by Django 4.2.2 on 2023-07-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('is_contacted', models.BooleanField(default=False)),
            ],
        ),
    ]