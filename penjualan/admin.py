from django.contrib import admin

from .models import DaftarBarang, Transaksi

# Register your models here.
admin.site.register(DaftarBarang)
admin.site.register(Transaksi)