# Generated by Django 2.2 on 2019-08-16 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0017_auto_20190806_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='court_address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_complete',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_court',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_group',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_level',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='game',
            name='league',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='game',
            name='team_a',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='game',
            name='team_a_group_no',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='Group'),
        ),
        migrations.AlterField(
            model_name='game',
            name='team_b',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='game',
            name='team_b_group_no',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='Group'),
        ),
        migrations.AlterField(
            model_name='team',
            name='league',
            field=models.CharField(blank=True, default='zjb', max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='league_year',
            field=models.CharField(blank=True, default='2019', max_length=10),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_company',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_group',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_group_no',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_level',
            field=models.CharField(blank=True, default='同一级别', max_length=10),
        ),
    ]
