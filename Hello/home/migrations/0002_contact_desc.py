# Generated by Django 4.0.2 on 2022-02-07 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]
