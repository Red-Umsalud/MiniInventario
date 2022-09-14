# Generated by Django 4.0.7 on 2022-09-14 15:10

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activo',
            fields=[
                ('id_activo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=1024, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=1024, null=True)),
                ('codigo', models.IntegerField()),
            ],
            options={
                'db_table': 'activo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id_fotografia', models.AutoField(primary_key=True, serialize=False)),
                ('fotografia', models.ImageField(blank=True, null=True, upload_to=app.models.renombrar)),
                ('tipo', models.IntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C')], default=0)),
                ('id_activo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.activo')),
            ],
            options={
                'db_table': 'fotografia',
                'managed': True,
            },
        ),
    ]
