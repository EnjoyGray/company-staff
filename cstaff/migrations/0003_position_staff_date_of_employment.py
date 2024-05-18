# Generated by Django 5.0.6 on 2024-05-16 11:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cstaff', '0002_alter_staff_name_alter_staff_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_staff', models.CharField(max_length=255, verbose_name='Position Title')),
                ('positionID', models.IntegerField(default=5, verbose_name='Position ID')),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
                'ordering': ['position_staff'],
            },
        ),
        migrations.AddField(
            model_name='staff',
            name='date_of_employment',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date of Employment'),
            preserve_default=False,
        ),
    ]