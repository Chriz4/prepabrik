from django.contrib import admin

from .models import Barang, Kasir, Transaksi, Pesan

# Register your models here.
admin.site.register(Barang)
admin.site.register(Kasir)
admin.site.register(Transaksi)
admin.site.register(Pesan)