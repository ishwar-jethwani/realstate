# Generated by Django 3.1.5 on 2021-01-27 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='service_10',
            field=models.CharField(blank=True, max_length=100, verbose_name='Service number five'),
        ),
        migrations.AddField(
            model_name='price',
            name='service_6',
            field=models.CharField(blank=True, max_length=100, verbose_name='Service'),
        ),
        migrations.AddField(
            model_name='price',
            name='service_7',
            field=models.CharField(blank=True, max_length=100, verbose_name='Service number two'),
        ),
        migrations.AddField(
            model_name='price',
            name='service_8',
            field=models.CharField(blank=True, max_length=100, verbose_name='Service number three'),
        ),
        migrations.AddField(
            model_name='price',
            name='service_9',
            field=models.CharField(blank=True, max_length=100, verbose_name='Service number four'),
        ),
        migrations.AlterField(
            model_name='price',
            name='service_1',
            field=models.CharField(blank=True, max_length=100, verbose_name='Service'),
        ),
        migrations.AlterField(
            model_name='price',
            name='service_2',
            field=models.CharField(blank=True, max_length=100, verbose_name='Service number two'),
        ),
        migrations.AlterField(
            model_name='price',
            name='service_3',
            field=models.CharField(blank=True, max_length=100, verbose_name='Service number three'),
        ),
        migrations.AlterField(
            model_name='price',
            name='service_4',
            field=models.CharField(blank=True, max_length=100, verbose_name='Service number four'),
        ),
        migrations.AlterField(
            model_name='price',
            name='service_5',
            field=models.CharField(blank=True, max_length=100, verbose_name='Service number five'),
        ),
        migrations.AlterField(
            model_name='price',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Package Name'),
        ),
    ]