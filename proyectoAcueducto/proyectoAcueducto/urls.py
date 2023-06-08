"""
URL configuration for proyectoAcueducto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include


from webapp.views import crudCliente, crudCuenta, crudBarrio, crudEstablecimiento, crearCliente, editarCliente, \
    eliminarCliente, crearEstablecimiento, editarEstablecimiento, eliminarEstablecimiento, crearBarrio,editarBarrio,eliminarBarrio, \
    crearCuenta, editarCuenta, eliminarCuenta, vistaAdmin, vistaTes, hisPagos, crudPagos, editarPagos, eliminarPagos, crudRecaudos, eliminarRecaudos, \
    vistaRec, detallesRecaudo, generarRecaudo, home, exit, crudUsuario, crearUsuario, editarUsuario, eliminarUsuario


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/',exit, name='exit'),
    path('',home, name='home'),
    path('admin/', admin.site.urls),
    path('vistaAdmin/', vistaAdmin, name='vistaAdmin'),
    path('vistaTes/', vistaTes, name='vistaTes'),
    path('vistaTes/hisPagos', hisPagos, name='hisPagos'),

    path('vistaRec/', vistaRec, name='vistaRec'),
    path('vistaRec/detallesRecaudo/<int:id>', detallesRecaudo, name='detallesRecaudo'),
    path('vistaRec/detallesRecaudo/generarRecaudo/<int:id>', generarRecaudo, name='generarRecaudo'),

    path('crudPagos/', crudPagos, name='crudPagos'),
    path('crudPagos/editarPagos/<int:id>', editarPagos, name='editarPagos'),
    path('crudPagos/eliminarPagos/<int:id>', eliminarPagos, name='eliminarPagos'),


    path('crudRecaudos/', crudRecaudos, name='crudRecaudos'),
    path('crudRecaudos/eliminarRecaudos/<int:id>', eliminarRecaudos, name='eliminarRecaudos'),

    path('crudCuenta/', crudCuenta, name='crudCuenta'),
    path('crudCuenta/crearCuenta/', crearCuenta, name='crearCuenta'),
    path('crudCuenta/editarCuenta/<int:id>', editarCuenta, name='editarCuenta'),
    path('crudCuenta/eliminarCuenta/<int:id>', eliminarCuenta,name='eliminarCuenta'),

    path('crudBarrio/', crudBarrio, name='crudBarrio'),
    path('crudBarrio/crearBarrio/', crearBarrio, name='crearBarrio'),
    path('crudBarrio/editarBarrio/<int:id>', editarBarrio, name='editarBarrio'),
    path('crudBarrio/eliminarBarrio/<int:id>', eliminarBarrio,name='eliminarBarrio'),

    path('crudUsuario',crudUsuario, name='crudUsuario'),
    path('crudUsuario/crearUsuario/',crearUsuario, name='crearUsuario'),
    path('crudUsuario/editarUsuario/<int:id>', editarUsuario, name='editarUsuario'),
    path('eliminarUsuario/<int:id>', eliminarUsuario, name='eliminarUsuario'),

    path('crudEstablecimiento/', crudEstablecimiento, name='crudEstablecimiento'),
    path('crudEstablecimiento/crearEstablecimiento/', crearEstablecimiento, name='crearEstablecimiento'),
    path('crudEstablecimiento/editarEstablecimiento/<int:id>', editarEstablecimiento, name='editarEstablecimiento'),
    path('crudEstablecimiento/eliminarEstablecimiento/<int:id>', eliminarEstablecimiento, name='eliminarEstablecimiento'),

    path('crudCliente/', crudCliente, name='crudCliente'),
    path('crudCliente/crearCliente/', crearCliente, name='crearCliente'),
    path('crudCliente/editarCliente/<int:id>', editarCliente, name='editarCliente'),
    path('crudCliente/eliminarCliente/<int:id>', eliminarCliente, name='eliminarCliente')
]
