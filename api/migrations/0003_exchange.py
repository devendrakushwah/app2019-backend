# Generated by Django 2.1.5 on 2019-01-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_image_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=200)),
            ],
        ),
    ]