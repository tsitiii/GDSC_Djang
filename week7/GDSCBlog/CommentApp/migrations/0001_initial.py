# Generated by Django 5.0.2 on 2024-02-26 12:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Content', models.TextField(max_length=250)),
                ('Author', models.CharField(max_length=50)),
                ('PublishedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogApp.postt')),
            ],
        ),
    ]