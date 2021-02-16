# Generated by Django 3.1.5 on 2021-02-16 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='paragraph',
            field=models.CharField(blank=True, max_length=300, verbose_name='Main Paragrph'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='point_1',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point one'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='point_2',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point two'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='point_3',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point three'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='overview',
            field=models.CharField(max_length=500, verbose_name='overview'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='career',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Post Name'),
        ),
        migrations.AlterField(
            model_name='career_header',
            name='title',
            field=models.CharField(max_length=150, verbose_name='image tittle'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=250, verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='point_1',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point one'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='point_10',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point Ten'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='point_11',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point Eleven'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='point_12',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point Twele'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='point_13',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point Thirteen'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='point_14',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point Fourteen'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='point_15',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point Fifteen'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='point_2',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point two'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='point_3',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point three'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='point_4',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point Four'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='point_5',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point Five'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='point_6',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point Six'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='point_7',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point Seven'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='point_8',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point Eight'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='point_9',
            field=models.CharField(blank=True, max_length=150, verbose_name='Point Nine'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='paragraph',
            field=models.CharField(max_length=150, verbose_name='Content Box'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='header',
            name='content',
            field=models.CharField(blank=True, max_length=500, verbose_name='Content Box'),
        ),
        migrations.AlterField(
            model_name='header',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='price',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Package Name'),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Title'),
        ),
    ]