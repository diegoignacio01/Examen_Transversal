 
from django.http import request
from django.views.decorators import csrf
from django.shortcuts import redirect, render
from rest_framework import serializers
import rest_framework
from .models import Proveedor
from .forms import ProveedorForm
from rest_framework.serializers import Serializer

from rest_framework.decorators import api_view, authentication_classes,permission_classes

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

def home(request):
    proveedores= Proveedor.objects.all()
    return render(request,'index.html',context={'datos':proveedores},
    
)

def registrar_proveedor(request):


    if request.method=='POST':
        proveedor_form=ProveedorForm(request.POST)
        if proveedor_form.is_valid():
            proveedor_form.save()
            return redirect('home')


    else:
        proveedor_form=ProveedorForm()
    return render(request,'core/registrar_proveedores.html',{'proveedor_form':proveedor_form})


def ver_proveedores(request):
    proveedores = Proveedor.objects.all()

    return render(request, 'core/ver.html', context={'proveedores':proveedores})


def modificar_proveedores(request,id):
    proveedor = Proveedor.objects.get(id=id)

    datos ={
        'form': ProveedorForm(instance=proveedor)
    }
    if request.method == 'POST': 
        formulario = ProveedorForm(data=request.POST, instance = proveedor)
        if formulario.is_valid: 
            formulario.save()
            return redirect('ver')
    return render(request, 'core/modificar_proveedor.html', datos)


#FUNCION PARA BUSCAR LOS DATOS DE UN PROVEEDOR EN ESPECIFICO
@api_view(['GET','PUT','DELETE'])
def detalle_proveedor(resquest,id):
    try:
        proveedor=Proveedor.objects.get(Idprovee=id)
    except Proveedor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if resquest.method == 'PUT':
        serializers = ProveedorSerializer(proveedor)
        return Response(serializers.data)
    if request.method == 'PUT':
        data =JSONParser().parse(request)
        serializers = ProveedorSerializer(proveedor,data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        proveedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



from rest_framework.serializers import Serializer
from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProveedorSerializer





#TODOS LOS DATOS DE LOS PROVEEDORES
@csrf_exempt
@api_view(['GET', 'POST'])



def lista_proveedores(request): 
    if request.method== 'GET':
        proveedor = Proveedor.objects.all()
        serializer =ProveedorSerializer(proveedor, many=True)
        return Response(serializer.data)

    elif request.method=='POST': 
        data = JSONParser().parse(request)
        serializer = ProveedorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def lista_api(request):
    return render(request, 'apiweb.html')