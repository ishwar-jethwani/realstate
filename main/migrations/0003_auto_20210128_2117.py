# Generated by Django 3.1.5 on 2021-01-28 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210128_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='paragraph',
            field=models.CharField(blank=True, max_length=100, verbose_name='Main Paragrph'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='point_1',
            field=models.CharField(blank=True, max_length=50, verbose_name='Point one'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='point_2',
            field=models.CharField(blank=True, max_length=50, verbose_name='Point two'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='point_3',
            field=models.CharField(blank=True, max_length=50, verbose_name='Point three'),
        ),
    ]
