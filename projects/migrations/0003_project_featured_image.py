# Generated by Django 3.2.8 on 2021-10-15 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20211015_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpeg', null=True, upload_to=''),
        ),
    ]
