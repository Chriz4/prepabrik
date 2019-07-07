from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class DaftarBarang(models.Model):
    nama = models.TextField(max_length=30)
    harga = models.IntegerField()

    def __str__(self):
        return self.nama


# class log_beli(models.Model):
#     barang = models.ForeignKey(DaftarBarang, on_delete=models.SET_NULL, null=True)
#     jumlah = models.IntegerField()
#     pembeli = models.OneToOneField()


class Transaksi(models.Model):
    barang = models.ForeignKey(
        DaftarBarang,
        on_delete=models.CASCADE
    )
    pembeli = models.CharField(max_length=30)
    telp = models.CharField(max_length=20)
    jumlah = models.IntegerField()
    harga = models.BigIntegerField()
    waktu = models.DateTimeField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return self.pembeli

    def get_absolute_url(self):
        return reverse('penjualan')