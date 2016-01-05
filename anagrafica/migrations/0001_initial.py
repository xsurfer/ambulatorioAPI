# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-05 03:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paziente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nome', models.CharField(max_length=50)),
                ('cognome', models.CharField(max_length=50)),
                ('sesso', models.CharField(choices=[('M', 'Maschio'), ('F', 'Femmina')], max_length=1)),
                ('data_nascita', models.DateField(blank=True, max_length=100)),
                ('nazionalita', django_countries.fields.CountryField(default='IT', max_length=2)),
                ('indirizzo_residenza', models.CharField(max_length=100)),
                ('comune_residenza', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=25, null=True)),
                ('cellulare', models.CharField(blank=True, max_length=25, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('profilo', models.TextField(blank=True, max_length=1000, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pazienti', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
                'db_table': 'pazienti',
            },
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('anamnesi', models.TextField(blank=True, max_length=1000, null=True)),
                ('esame_obiettivo', models.TextField(blank=True, max_length=1000, null=True)),
                ('esame_strumentale', models.TextField(blank=True, max_length=1000, null=True)),
                ('diagnosi', models.TextField(blank=True, max_length=1000, null=True)),
                ('terapia', models.TextField(blank=True, max_length=1000, null=True)),
                ('data_visita', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visite', to=settings.AUTH_USER_MODEL)),
                ('paziente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visite', to='anagrafica.Paziente')),
            ],
            options={
                'ordering': ('created',),
                'db_table': 'visite',
            },
        ),
    ]