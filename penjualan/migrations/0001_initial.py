# Generated by Django 2.2 on 2019-06-19 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DaftarBarang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField(max_length=30)),
                ('harga', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pembeli', models.TextField(max_length=30)),
                ('jumlah', models.IntegerField()),
                ('harga', models.BigIntegerField()),
                ('waktu', models.DateTimeField()),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='penjualan.DaftarBarang')),
            ],
        ),
    ]