# Generated by Django 2.1.7 on 2019-02-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('which_angel', models.CharField(max_length=30, unique=True)),
                ('total', models.CharField(max_length=4)),
                ('right', models.CharField(max_length=4)),
                ('wrong', models.CharField(max_length=4)),
                ('list', models.CharField(max_length=1000)),
                ('subject', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='math',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('which_angel', models.CharField(max_length=40)),
                ('total', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='math_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('which_angel', models.CharField(max_length=40)),
                ('total', models.CharField(max_length=10)),
            ],
        ),
    ]