# Generated by Django 2.2 on 2019-07-08 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.CharField(max_length=20, unique=True)),
                ('team_name', models.CharField(max_length=100)),
                ('team_company', models.CharField(max_length=100)),
                ('team_level', models.CharField(max_length=10)),
                ('team_group', models.CharField(max_length=10)),
                ('team_credit', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
