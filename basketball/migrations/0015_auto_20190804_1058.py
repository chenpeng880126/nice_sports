# Generated by Django 2.2 on 2019-08-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0014_team_team_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_rank',
            field=models.CharField(blank=True, default='', max_length=2, null=True),
        ),
    ]
