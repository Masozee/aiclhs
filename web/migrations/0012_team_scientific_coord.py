# Generated by Django 3.2.4 on 2021-08-07 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_team_panggilan'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='scientific_coord',
            field=models.BooleanField(default=False),
        ),
    ]
