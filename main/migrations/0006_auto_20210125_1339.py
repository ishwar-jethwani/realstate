# Generated by Django 3.1.5 on 2021-01-25 08:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210125_1320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'ordering': ['-number']},
        ),
        migrations.AddField(
            model_name='testimonial',
            name='prop_img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='realestate/testimonial', verbose_name='Project Image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='social_link_f',
            field=models.URLField(blank=True, default='facebook.com'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='social_link_i',
            field=models.URLField(blank=True, default='instagram.com'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='social_link_l',
            field=models.URLField(blank=True, default='linkedin.com'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='social_link_t',
            field=models.URLField(blank=True, default='twiter.com'),
        ),
    ]
