# Generated by Django 2.2.4 on 2019-09-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamamsazeh', '0006_auto_20190905_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='genre',
            field=models.CharField(choices=[('1', 'Oil, Gas and Petrochemical'), ('2', 'Educational and Cultural Structures'), ('3', 'Steal Structures and Bridges'), ('4', 'Industrial and Civil Structure'), ('5', 'Mass production'), ('6', 'Road construction'), ('7', 'Others')], default='7', max_length=2),
        ),
    ]
