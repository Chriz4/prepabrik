# Generated by Django 2.2 on 2019-07-18 14:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('penjualan', '0004_auto_20190718_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=20)),
                ('harga', models.IntegerField()),
                ('jumlah', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kasir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pembeli', models.CharField(max_length=20)),
                ('total', models.BigIntegerField(blank=True, default=0, null=True)),
                ('waktu', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='penjualan.Kasir')),
            ],
        ),
        migrations.CreateModel(
            name='Pesan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.IntegerField()),
                ('harga', models.BigIntegerField(blank=True, default=0, null=True)),
                ('barang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='penjualan.Barang')),
                ('transaksi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='penjualan.Transaksi')),
            ],
        ),
    ]
