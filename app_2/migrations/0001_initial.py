# Generated by Django 3.2 on 2021-04-18 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeAct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_activity', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndEntr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('ident_number', models.CharField(blank=True, max_length=50, null=True)),
                ('tel_number', models.CharField(blank=True, max_length=11, null=True)),
                ('channel', models.CharField(blank=True, max_length=10, null=True)),
                ('el_key', models.BooleanField(default=True)),
                ('status', models.BooleanField(default=True)),
                ('reg_date', models.DateField()),
                ('end_date', models.DateField()),
                ('type_of_activity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_2.typeact')),
            ],
        ),
    ]