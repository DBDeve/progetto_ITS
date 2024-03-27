# Generated by Django 5.0.3 on 2024-03-27 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applicazione', '0007_rename_date_clients_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('codice_fiscale', models.CharField(default='', max_length=200)),
                ('iban', models.IntegerField(default=0)),
                ('mail', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='stipendio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stipendio_ore', models.IntegerField(default=0)),
                ('giorni_lavorati', models.IntegerField(default=0)),
                ('ore_lavorate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='promotions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicazione.clients')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('prize', models.IntegerField(default=0)),
                ('stato', models.CharField(choices=[('libera', 'libera'), ('prenotata', 'prenotata'), ('occupata', 'occupata'), ('non disponibile', 'non disponibile')], default='non disponibile', max_length=15)),
                ('clienti_ospitabili', models.IntegerField(default=0)),
                ('appunto_gestore', models.CharField(default='', max_length=200)),
                ('appunti_cliente', models.CharField(default='', max_length=200)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='applicazione.clients')),
            ],
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('prize', models.IntegerField(default=0)),
                ('NumberOfUse', models.IntegerField(default=0)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicazione.clients')),
            ],
        ),
    ]
