# Generated by Django 2.1.5 on 2019-01-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('cmc_rank', models.IntegerField(max_length=10, null=True)),
                ('symbol', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('price_usd', models.CharField(max_length=200, null=True)),
                ('total_supply', models.CharField(max_length=200, null=True)),
                ('max_supply', models.CharField(max_length=200, null=True)),
                ('circulating_supply', models.CharField(max_length=200, null=True)),
                ('change_hour', models.CharField(max_length=200, null=True)),
                ('change_day', models.CharField(max_length=200, null=True)),
                ('change_week', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('symbol', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
            ],
        ),
    ]
