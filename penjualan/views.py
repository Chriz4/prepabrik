from django.shortcuts import render, redirect
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .render import Render

from .models import Kasir, Barang, Transaksi, Pesan

# Create your views here.
def home(request):
    template_name = 'penjualan/log_transaksi.html'
    tran = Transaksi.objects.all()
    return render(request, template_name, {'logs':tran})


@login_required
def pesanan(request, transaksi_id):
    template_name = 'penjualan/log_pesanan.html'
    selected_tran = Transaksi.objects.get(id=transaksi_id)
    pesanan = Pesan.objects.filter(transaksi__id=selected_tran.id).values('id', 'barang__nama', 'jumlah', 'harga', 'transaksi__id', 'transaksi__user__nama')
    context = {'pesanan':pesanan, 'user':request.user, 'selected_tran':selected_tran}
    return render(request, template_name, context)


@login_required
def generate(request, transaksi_id):
    selected_tran = Transaksi.objects.get(id=transaksi_id)
    pesanan = Pesan.objects.filter(transaksi__id=selected_tran.id).values('id', 'barang__nama', 'jumlah', 'harga', 'transaksi__id', 'transaksi__user__nama')
    params = {
        'selected_tran': selected_tran,
        'pesanan' : pesanan,
    }
    return Render.render('penjualan/document.html', params)


@login_required
def transaksi(request):
    list_barang = Barang.objects.all()
    context = {'user':request.user, 'list_barang':list_barang}
    if request.method == 'POST':
        jtutup = request.POST['barang1']
        jgalon = request.POST['barang2']
        jsaring = request.POST['barang3']
        jtutup = int(jtutup)
        jgalon = int(jgalon)
        jsaring = int(jsaring)
        # Simpan Kasir
        form = request.POST
        name = form['kasir']
        current_kasir = Kasir(nama=name)
        current_kasir.save()
        # Masukkan Kasir ke transaksi
        pesanan = Transaksi(user=current_kasir, pembeli=form['pembeli'], disetujui=form['penyetuju'], dibayar=form['dibayar'])
        pesanan.save()
        # Masukan Pesanan ke Transaksi
        tutup = Barang.objects.get(nama='Tutup')
        galon = Barang.objects.get(nama='Galon')
        saring = Barang.objects.get(nama='Saring')
        pesanan.pesan_set.create(barang=tutup, jumlah=jtutup, harga=jtutup*tutup.harga)
        pesanan.pesan_set.create(barang=galon, jumlah=jgalon, harga=jgalon*galon.harga)
        pesanan.pesan_set.create(barang=saring, jumlah=jsaring, harga=jsaring*saring.harga)
        htutup = pesanan.pesan_set.get(barang=tutup)
        hgalon = pesanan.pesan_set.get(barang=galon)
        hsaring = pesanan.pesan_set.get(barang=saring)
        pesanan.total = htutup.harga + hgalon.harga + hsaring.harga
        pesanan.save()
        return redirect('penjualan')
    return render(request, 'penjualan/transaksi.html', context)

