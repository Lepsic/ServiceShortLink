# Generated by Django 4.2 on 2023-05-12 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_link', models.CharField(max_length=528)),
                ('update_link', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
