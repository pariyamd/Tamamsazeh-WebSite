# Generated by Django 2.2.4 on 2019-09-05 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamamsazeh', '0004_auto_20190905_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='genre',
            field=models.CharField(choices=[(1, 'Oil, Gas and Petrochemical'), (2, 'Educational and Cultural Structures'), (3, 'Steal Structures and Bridges'), (4, 'Industrial and Civil Structure'), (5, 'Mass production'), (6, 'Road construction'), (7, 'Others')], default='7', max_length=2),
        ),
    ]
