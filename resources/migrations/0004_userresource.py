# Generated by Django 5.0.4 on 2024-04-27 17:39

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_remove_domain_id_remove_resource_id_domain_uuid_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResource',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('saved', models.BooleanField(default=False)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interests', to='resources.resource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domains', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'resource')},
            },
        ),
    ]