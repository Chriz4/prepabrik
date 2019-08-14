from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Barang(models.Model):
    nama = models.CharField(max_length=20)
    harga = models.IntegerField()
    jumlah = models.IntegerField()

    def __str__(self):
        return self.nama


class Kasir(models.Model):
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama
        

class Transaksi(models.Model):
    now = datetime.datetime.now()
    user = models.ForeignKey(Kasir, on_delete=models.CASCADE)
    pembeli = models.CharField(max_length=20)
    disetujui = models.CharField(max_length=20)
    dibayar = models.CharField(max_length=20)
    total = models.BigIntegerField(default=0, null=True, blank=True)
    waktu = models.DateTimeField(default=now)

    def __str__(self):
        return self.pembeli

class Pesan(models.Model):
    barang = models.ForeignKey(Barang, on_delete=models.SET_NULL, null=True)
    jumlah = models.IntegerField()
    harga = models.BigIntegerField(default=0, null=True, blank=True)
    transaksi = models.ForeignKey(Transaksi, on_delete=models.CASCADE)