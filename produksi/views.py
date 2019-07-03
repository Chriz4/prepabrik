from django.shortcuts import render, redirect
from django.db.models import Sum

from .models import LogBarang, ListBarang
from .forms import LogBarangModelForm

import datetime

# Create your views here.
def produksi_list(request):
    template_name = "produksi/list-produksi.html"
    log_barang = LogBarang.objects.all().order_by('-waktu')
    page_title = "Log Produksi"
    # Hitung total semua barang
    qbarang = LogBarang.objects.all().aggregate(Sum('jumlah'))
    jumlah_barang = qbarang['jumlah__sum']
    #Hitung total masing-masing barang
    jenis_barang = ListBarang.objects.all()
    dictmasing = {}
    for brg in range(1, ListBarang.objects.all().count()+1):
        dictmasing.update({jenis_barang[brg-1]:LogBarang.objects.filter(barang=brg).aggregate(Sum('jumlah'))['jumlah__sum']})
    # print(jumlah_barang)
    context = {"page_title":page_title, "log_barang": log_barang, "jumlah_barang":jumlah_barang, "dictmasing":dictmasing, "jenis_barang":jenis_barang}
    return render(request, template_name, context)


def tambah_barang(request):
    form = LogBarangModelForm(request.POST or None)
    if form.is_valid():
        # print(form)
        obj = form.save(commit=False)
        obj.waktu = datetime.datetime.now()
        obj.save()
        return redirect('/produksi')
        # form = LogBarangModelForm()
    template_name = "produksi/form.html"
    context = {'form':form}
    return render(request, template_name, context)