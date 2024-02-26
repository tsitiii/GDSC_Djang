# Generated by Django 5.0.2 on 2024-02-26 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50, unique=True)),
                ('Content', models.TextField(max_length=250)),
                ('Category', models.CharField(max_length=50)),
                ('Image', models.ImageField(upload_to='')),
            ],
        ),
    ]
