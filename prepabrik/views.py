from django.http import HttpResponse
from django.shortcuts import render

from produksi.models import LogBarang

def home_page(request):
    ls = LogBarang.objects.all()[:3]
    title = 'Sistem Informasi Pabrik'
    template_name = "home.html"
    context = {"title": title,'list_barang':ls}
    return render(request, template_name, context)