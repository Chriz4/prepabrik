
from django.contrib import admin
from django.urls import path, include

from .views import home_page

from produksi.views import (
    produksi_list,
    tambah_barang
    )

from penjualan import views as penjualan

urlpatterns = [
    path('', home_page, name='home'),
    path('produksi/', produksi_list, name='produksi'),
    path('tambah/', tambah_barang, name='tambah'),
    path('penjualan/', penjualan.home, name='penjualan'),
    path('pesanan/<int:transaksi_id>/', penjualan.pesanan, name='pesanan'),
    path('transaksi/', penjualan.transaksi, name='transaksi'),
    path('dokumen/<int:transaksi_id>/', penjualan.generate),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
