# Generated by Django 5.0.3 on 2024-04-15 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0003_alter_rooms_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GoOut',
            new_name='Expense',
        ),
    ]