# Generated by Django 3.2.3 on 2021-05-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveCases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('last_day', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NegativeSamples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('last_day', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PositiveSamples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('last_day', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuarantineAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('reason', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TotalSamples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('last_day', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaitingSamples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('last_day', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
