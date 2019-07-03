from django.contrib import admin

from .models import ListBarang, LogBarang

# Register your models here.
admin.site.register(ListBarang)
admin.site.register(LogBarang)
