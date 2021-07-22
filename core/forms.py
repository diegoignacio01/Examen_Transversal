#LISTA


from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.db.models import fields
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria,Proveedor


class ProveedorForm(ModelForm):

    class Meta:
        model=Proveedor
        fields=['id','fotografia','nombre','telefono','direccion','email','pais','contraseña','moneda']
        labels ={
            'id':'ingrese el numero identificador de el proveedor',
            'fotografia':'Carge la fotografia que identifique al proveedor(logo)',
            'nombre':'Ingrese nombre completo del proveedor',
            'telefono':'Ingrese numero telefonico de proveedor',
            'direccion':'Ingrese direccion de proveedor',
            'email':'Ingrese email de proveedor',
            'pais':'Ingrese pais de proveedor',
            'contraseña':'la contraseña se generara automaticamente',
            'moneda':'Ingrese el tipo de moneda con que se realizara el pago'

        }
        widgets= {
            'id':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'id proveedor',
                    'id':'id'
                }
            ),

            'fotografia':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'fotografia',
                    'id':'fotografia'
                }
            ),

            'telefono':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'telefono',
                    'id':'telefono'
                }
            ),
            'direccion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'direccion',
                    'id':'direccion'
                }
            ),
            'email':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'email',
                    'id':'email'
                }
            ),
            'pais':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'pais',
                    'id':'pais'
                }
            ),
            'contraseña':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'contraseña',
                    'id':'contraseña'
                }
            ),
            'moneda':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'moneda',
                    'id':'moneda'
                }
            ),
            'categoria':forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'categoria',
                    'id':'categoria'
                }
            ),

 }