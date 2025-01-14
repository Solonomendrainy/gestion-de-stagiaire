# Generated by Django 5.0.4 on 2024-09-20 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stagiaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cin', models.IntegerField()),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.IntegerField()),
                ('findustage', models.BooleanField(default=False)),
                ('qualite', models.TextField()),
                ('etablissement', models.TextField()),
            ],
        ),
    ]
