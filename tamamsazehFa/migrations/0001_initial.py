# Generated by Django 2.2.4 on 2019-09-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tamamsazeh', '0007_auto_20190908_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleFa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('date', models.DateField(blank=True, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='articles/')),
                ('author', models.CharField(blank=True, default='unknown', max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostFa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('date', models.DateField(blank=True, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='articles/')),
                ('text', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectFa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('info', models.TextField(blank=True)),
                ('genre', models.CharField(choices=[('1', 'Oil, Gas and Petrochemical'), ('2', 'Educational and Cultural Structures'), ('3', 'Steal Structures and Bridges'), ('4', 'Industrial and Civil Structure'), ('5', 'Mass production'), ('6', 'Road construction'), ('7', 'Others')], default='7', max_length=2)),
                ('Album', models.ManyToManyField(blank=True, to='tamamsazeh.ProjectImage')),
            ],
        ),
    ]