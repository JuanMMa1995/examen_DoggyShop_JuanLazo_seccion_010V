from django.urls import path, include
from .views import index, galeriaDeAdopcion, quienesSomos, contacto, productos, agregar_productos, listar_productos, modificar_productos, eliminar_producto, registro, ProductoViewset, agregar_carro, elimar_carro, restar_carro, limpiar_carro
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)

urlpatterns = [
    path('', index, name="index"),
    path('galeriaDeAdopcion/', galeriaDeAdopcion, name="galeriaDeAdopcion"),
    path('quienesSomos/', quienesSomos, name="quienesSomos"),
    path('contacto/', contacto, name="contacto"),
    path('productos/', productos, name="productos"),
    path('agregar_productos/', agregar_productos, name="agregar_productos"),
    path('listar_productos/', listar_productos, name="listar_productos"),
    path('modificar_productos/<id>/', modificar_productos, name="modificar_productos"),
    path('eliminar_producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
    path('agregar/<int:producto_id>', agregar_carro, name="Add" ),
    path('eliminar/<int:producto_id>', elimar_carro, name="Del" ),
    path('restar/<int:producto_id>', restar_carro, name="Sub" ),
    path('limpiar/', limpiar_carro, name="CLS" ),
]
