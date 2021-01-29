# Generated by Django 3.1.5 on 2021-01-29 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210129_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career_header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='image tittle')),
                ('img', models.ImageField(upload_to='', verbose_name='Image For Career Page')),
                ('date', models.DateField(auto_now_add=True)),
                ('number', models.IntegerField(verbose_name='Serial Number')),
            ],
            options={
                'ordering': ['-number'],
            },
        ),
    ]