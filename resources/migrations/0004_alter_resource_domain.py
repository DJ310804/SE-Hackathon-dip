# Generated by Django 5.0.4 on 2024-04-28 02:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_domain_id_alter_domain_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.domain'),
        ),
    ]
