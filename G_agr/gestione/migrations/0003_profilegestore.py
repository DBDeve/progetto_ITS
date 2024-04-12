# Generated by Django 5.0.3 on 2024-04-03 10:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0002_alter_room_client'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileGestore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestione.room')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestione.employee')),
                ('gestore', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('promotions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestione.promotions')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestione.services')),
            ],
        ),
    ]