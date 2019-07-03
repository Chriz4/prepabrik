from django.db import models
# import datetime

# Create your models here.
class ListBarang(models.Model):
    nama = models.TextField(max_length=30)

    def __str__(self):
        return self.nama

class LogBarang(models.Model):
    # now = datetime.datetime.now()
    barang = models.ForeignKey(
        ListBarang, on_delete=models.CASCADE
    )
    jumlah = models.IntegerField()
    waktu = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
