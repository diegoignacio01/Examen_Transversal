#LISTA

from django.db import models


class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True, verbose_name='Id categoria')
    nombreCategoria=models.CharField(max_length=60 ,verbose_name='Nombre categoria')

    def __str__(self):
        return (self.nombreCategoria)
    


class Proveedor(models.Model):
    IDProve=models.CharField(max_length=4,primary_key=True,verbose_name='Id proveedor')
    Fotografia=models.ImageField(upload_to='images/', null=True, blank=True)
    NombreCompleto=models.CharField(max_length=50,verbose_name='Nombre completo proveedor')
    Telefono=models.CharField(max_length=12,verbose_name='Telefono proveedor')
    Direccion=models.CharField(max_length=50,verbose_name='Direccion proveedor')
    Email=models.CharField(max_length=60,verbose_name='Email proveedor')
    Pais=models.CharField(max_length=20,verbose_name='Pais proveedor')
    Contraseña=models.CharField(max_length=10,verbose_name='Contraseña proveedor')
    MonedaPago=models.CharField(max_length=6,verbose_name='Moneda de pago(pesos/dolares)')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return(self.idProve)
