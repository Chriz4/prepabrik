from django.shortcuts import render
from django.views.generic import CreateView

from .models import Transaksi, DaftarBarang

# Create your views here.
def penjualan_list(request):
    template_name = "penjualan/penjualan-list.html"
    qs = Transaksi.objects.all()
    context = { "page_title": "Log Transaksi", "object_list": qs }
    return render(request, template_name, context)

def transaksi(request):
    template_name = "penjualan/transaksi.html"
    print(request.POST)
    qs = DaftarBarang.objects.all()
    context = { "page_title": "Transaksi", "barang": qs }
    return render(request, template_name, context)

# class TransactionCreate(CreateView):
#     model = Transaksi
#     fields = ['barang', 'pembeli', 'telp', 'jumlah', 'harga']