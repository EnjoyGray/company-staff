# Generated by Django 5.0.6 on 2024-05-16 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cstaff', '0003_position_staff_date_of_employment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='positionID',
            field=models.IntegerField(default=6, verbose_name='Position ID'),
        ),
    ]