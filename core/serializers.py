from rest_framework import serializers 
from .models import Proveedor 

#CONVERTIR DATOS DE MANERA FACIL
class ProveedorSerializers(serializers.ModelSerializers):
    class Meta:
        model = Proveedor
        fields = ['id','nombre','telefono','direccion','email','pais','contraseña','moneda'] 