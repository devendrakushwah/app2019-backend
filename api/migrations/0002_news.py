# Generated by Django 2.1.5 on 2019-01-30 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100000)),
                ('image', models.URLField()),
                ('url', models.URLField()),
                ('date', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
            ],
        ),
    ]