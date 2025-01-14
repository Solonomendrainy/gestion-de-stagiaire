# Generated by Django 5.0.4 on 2024-11-27 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stagiairesencours', '0002_stagiairesencours_etablissement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('critere', models.CharField(max_length=200)),
                ('note', models.DecimalField(decimal_places=2, max_digits=5)),
                ('commentaires', models.TextField(blank=True, null=True)),
                ('date_evaluation', models.DateField(auto_now_add=True)),
                ('stagiaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stagiairesencours.stagiairesencours')),
            ],
        ),
    ]
