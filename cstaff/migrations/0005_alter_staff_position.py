# Generated by Django 5.0.6 on 2024-05-16 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cstaff', '0004_alter_position_positionid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cstaff.position', verbose_name='Position'),
        ),
    ]