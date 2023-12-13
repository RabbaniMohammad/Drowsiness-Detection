# Generated by Django 4.2.3 on 2023-10-24 23:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0006_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectWarnings',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('warning', models.CharField(blank=True, max_length=10, null=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
