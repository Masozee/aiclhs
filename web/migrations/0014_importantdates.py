# Generated by Django 3.2.4 on 2021-08-31 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_pembicara_panggilan'),
    ]

    operations = [
        migrations.CreateModel(
            name='importantdates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Judul', models.CharField(max_length=150)),
                ('Tanggal', models.CharField(max_length=50)),
                ('urutan', models.PositiveIntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'tanggal penting',
                'verbose_name_plural': 'tanggal penting',
            },
        ),
    ]