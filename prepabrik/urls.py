
from django.contrib import admin
from django.urls import path

from .views import home_page

from produksi.views import (
    produksi_list,
    tambah_barang
    )

from penjualan.views import (penjualan_list, transaksi )


urlpatterns = [
    path('', home_page),
    path('produksi/', produksi_list, name='produksi'),
    path('tambah/', tambah_barang, name='tambah'),
    path('penjualan/', penjualan_list, name='penjualan'),
    # path('transaksi/', TransactionCreate.as_view(), name='transaksi'),
    path('transaksi/', transaksi, name='transaksi'),
    path('admin/', admin.site.urls),
]
