# Generated by Django 3.2.3 on 2021-05-18 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indentr',
            options={'ordering': ['type_of_activity'], 'verbose_name': 'ИП', 'verbose_name_plural': 'ИП'},
        ),
        migrations.AlterModelOptions(
            name='indentrinfo',
            options={'ordering': ['iep'], 'verbose_name': 'ИП (Банк)', 'verbose_name_plural': 'ИП (Банки)'},
        ),
        migrations.AlterField(
            model_name='address',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_1.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='address',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_1.contract', verbose_name='Договор'),
        ),
        migrations.AlterField(
            model_name='address',
            name='kofa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_1.kindofactivity', verbose_name='Вид деятельности'),
        ),
        migrations.AlterField(
            model_name='cashboxes',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_1.address', verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='cashboxes',
            name='cashb_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_1.cashbname', verbose_name='Модель кассы'),
        ),
        migrations.AlterField(
            model_name='cashboxes',
            name='iep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_1.indentr', verbose_name='ИП'),
        ),
        migrations.AlterField(
            model_name='indentr',
            name='type_of_activity',
            field=models.CharField(blank=True, choices=[('ОДИНОЧКА', 'Одиночка'), ('ЦВЕТЫ', 'Цветы'), ('СМЦ', 'СМЦ'), ('СОЛДАТ', 'Солдат'), ('ЦВЕТЫ СОЛДАТ', 'Цветы солдат')], max_length=50, null=True, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='indentrinfo',
            name='bank',
            field=models.CharField(blank=True, choices=[('СБЕРБАНК', 'Сбербанк'), ('АЛЬФАБАНК', 'Альфа-Банк'), ('ТОЧКАБАНК', 'Точка'), ('РАЙФФАЙЗЕН', 'Райффайзен'), ('ТИНЬКОФФ', 'Тинькофф'), ('ВТБ', 'ВТБ')], max_length=50, null=True, verbose_name='Банк'),
        ),
        migrations.AlterField(
            model_name='indentrinfo',
            name='iep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_1.indentr', verbose_name='ИП'),
        ),
        migrations.AlterField(
            model_name='terminals',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_1.address', verbose_name='Адрес'),
        ),
    ]
