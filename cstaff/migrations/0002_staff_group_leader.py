# Generated by Django 5.0.6 on 2024-06-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cstaff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='group_leader',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Leader Group'),
        ),
    ]
