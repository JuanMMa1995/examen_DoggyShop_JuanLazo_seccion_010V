from django.db import models

# Create your models here. []

class Marca(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True, verbose_name='Codigo') 
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    precio = models.IntegerField()
    fec_ven = models.DateField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.codigo

opciones_consulta = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_Consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    aviso = models.BooleanField()

    def __str__(self):
        return self.nombre