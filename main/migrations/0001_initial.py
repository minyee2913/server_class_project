# Generated by Django 5.1.4 on 2024-12-05 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('order', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('headSetId', models.IntegerField()),
                ('score', models.FloatField()),
                ('success', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ProblemSet',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('successCount', models.IntegerField()),
                ('maxCount', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
