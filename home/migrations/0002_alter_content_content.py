# Generated by Django 4.0.1 on 2022-01-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
