from django.contrib import admin
from .models import Marca, Producto,Contacto
from .forms import ProductoForm
# Register your models here.[]

class ProductoAdmin(admin.ModelAdmin):
    list_display= ["codigo", "nombre", "marca", "precio", "fec_ven", "imagen"]
    list_editable= ["precio"]
    search_fields = ["codigo"]
    list_filter = ["marca"]
    list_per_page = 10
    form = ProductoForm

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)