# Generated by Django 4.2 on 2024-12-20 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('country', models.CharField(max_length=100, verbose_name='Davlati')),
            ],
        ),
        migrations.CreateModel(
            name='Gullar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('price', models.IntegerField(verbose_name='Narxi')),
                ('number', models.IntegerField(verbose_name='Soni')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blok.turlar', verbose_name='Brendi')),
            ],
        ),
    ]
