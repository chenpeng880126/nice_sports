# Generated by Django 2.2 on 2019-08-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0015_auto_20190804_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_rank',
            field=models.CharField(blank=True, default='', max_length=2, null=True, verbose_name='排名'),
        ),
    ]