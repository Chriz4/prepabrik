from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

from produksi.models import LogBarang
from penjualan.models import Transaksi

# @login_required
def home_page(request):
    ls = LogBarang.objects.all()[:3]
    lp = Transaksi.objects.all()[:3]
    title = 'Sistem Informasi Pabrik'
    template_name = "home.html"
    context = {"title": title,'list_barang':ls, 'list_jual':lp}
    return render(request, template_name, context)