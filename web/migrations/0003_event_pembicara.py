# Generated by Django 3.2.4 on 2021-07-08 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20210701_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Pembicara',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='web.pembicara'),
        ),
    ]