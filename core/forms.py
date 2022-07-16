from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields= '__all__'

class ProductoForm (forms.ModelForm):
    
    nombre = forms.CharField(min_length= 3, max_length=50)
    imagen = forms.ImageField(validators=[MaxSizeFileValidator(max_file_size=10)])
    precio = forms.IntegerField(min_value=150, max_value=150000)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("Este nombre ya existe")

        return nombre

    class Meta:
        model = Producto
        fields= '__all__'
    
    widgets = {
        "fec_ven": forms.SelectDateWidget()
    }

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username',"first_name", "last_name", "password1", "password2"]


