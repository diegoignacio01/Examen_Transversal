from django.urls import path
from .views import home, registrar_proveedor,modificar_proveedor,ver, lista_proveedores,lista_api,detalle_proveedor
from .viewsLogin import login

urlpatterns=[ 
    path('',home, name='home'),
    path('registrar_proveedor', registrar_proveedor, name="registrar_proveedor"),
    path('ver', ver, name="ver"),
    path('modificar_proveedor/<id>', modificar_proveedor, name="modificar_proveedor"),
    path('lista_proveedores', lista_proveedores, name="lista_proveedores"),
    path('lista_api', lista_api, name="lista_api"),
    path('detalle_proveedor',detalle_proveedor, name="detalle_proveedor"),
    path('login', login, name="login"),
]
