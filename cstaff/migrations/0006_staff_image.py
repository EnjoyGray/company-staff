# Generated by Django 5.0.6 on 2024-05-19 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cstaff', '0005_alter_staff_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Image profil'),
        ),
    ]
