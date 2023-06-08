from django.db.models import Sum
from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from user.forms import Meme, FormUser
from user.models import Tipo, User
from webapp.forms import FormCliente, FormEstablecimiento, FormBarrio, FormCuenta, FormPago, FormPago2
from webapp.models import Cliente, Cuenta, Barrio, Establecimiento, Pagos, Recaudos

# Create your views here.


@login_required
def home(request):
    tipo = request.user.tipo.id
    print(tipo)
    if ((tipo == 1) and (request.user.is_superuser == True)):
        return redirect('vistaAdmin')
    elif ((tipo == 2) and (request.user.is_superuser == True)):
        return redirect('vistaTes')
    elif ((tipo == 3) and (request.user.is_superuser == True)):
        return redirect('vistaRec')
    return HttpResponse('Este usuario no tiene permiso de acceder a la plataforma')
    client = Socrata("www.datos.gov.co", None)

    # esta funcion desenpaqueta los datos extraidos de la nube y retorna los datos con los filtros especificados
    def bajar_datos(limite_datos, departamento, columnas):
        results = client.get("gt2j-8ykr", limit=limite_datos, departamento_nom=departamento)
        results_df = pd.DataFrame.from_records(results)
        return results_df.loc[:, columnas]



def exit(request):
    logout(request)
    return redirect(home)

@login_required
def crudCliente(request):
    if request.user.tipo.id == 1:
        no_clientes = Cliente.objects.filter(estado=True).count()
        clientes = Cliente.objects.filter(estado=True)
        mensajes = {'msg1': 'Valor mensaje 1', 'no_clientes': no_clientes, 'clientes': clientes}
        return render(request,'cliente/crudCliente.html', mensajes)
    else:
        return redirect('exit')
#FormCliente = modelform_factory(Cliente, exclude=[])

@login_required
def crearCliente(request):
    if request.user.tipo.id ==1:
        if request.method == 'POST':
            formaCliente = FormCliente(request.POST)
            if formaCliente.is_valid():
                formaCliente.save()
                return redirect('crudCliente')
        else:
            formaCliente = FormCliente()
        datos = {'formaCliente': formaCliente}
        return render(request, 'cliente/crearCliente.html', datos)
    else:
        return redirect('exit')


@login_required
def editarCliente(request,id):
    if request.user.tipo.id == 1:
        cliente = get_object_or_404(Cliente, pk=id)
        if request.method == 'POST':
            formaCliente = FormCliente(request.POST, instance=cliente)
            if formaCliente.is_valid():
                formaCliente.save()
                return redirect('crudCliente')
        else:
            formaCliente = FormCliente(instance=cliente)
        datos = {'formaCliente': formaCliente}
        return render(request, 'cliente/editarCliente.html', datos)
    else:
        return redirect('exit')


@login_required
def eliminarCliente(request,id):
    if request.user.tipo.id == 1:
        cliente = get_object_or_404(Cliente, pk=id)
        if cliente:
            cliente.estado = False
            cliente.save()
        return redirect('crudCliente')
    else:
        return redirect('exit')

@login_required
def crudCuenta(request):
    if request.user.tipo.id == 1:
        no_cuentas = Cuenta.objects.filter(estado=True).count()
        cuentas = Cuenta.objects.filter(estado=True)
        datos = {'no_cuentas': no_cuentas, 'cuentas': cuentas}
        return render(request,'cuenta/crudCuenta.html', datos)
    else:
        return redirect('exit')

@login_required
def crearCuenta(request):
    if request.user.tipo.id == 1:
        if request.method == 'POST':
            formaCuenta = FormCuenta(request.POST)
            if formaCuenta.is_valid():
                formaCuenta.save()
                return redirect('crudCuenta')
        else:
            formaCuenta = FormCuenta()
        datos = {'formaCuenta': formaCuenta}
        return render(request, 'cuenta/crearCuenta.html', datos)
    else:
        return redirect('exit')

@login_required
def editarCuenta(request, id):
    if request.user.tipo.id == 1:
        cuenta = get_object_or_404(Cuenta, pk=id)
        if request.method == 'POST':
            formaCuenta = FormCuenta(request.POST, instance=cuenta)
            if formaCuenta.is_valid():
                formaCuenta.save()
                return redirect('crudCuenta')
        else:
            formaCuenta = FormCuenta(instance=cuenta)
        datos = {'formaCuenta': formaCuenta}
        return render(request, 'cuenta/editarCuenta.html', datos)
    else:
        return redirect('exit')

@login_required
def eliminarCuenta(request, id):
    if request.user.tipo.id == 1:
        cuenta = get_object_or_404(Cuenta, pk=id)
        if cuenta:
            cuenta.estado = False
            cuenta.save()
        return redirect('crudCuenta')
    else:
        return redirect('exit')

@login_required
def crudBarrio(request):
    if request.user.tipo.id == 1:
        no_barrios = Barrio.objects.filter(estado=True).count()
        barrios = Barrio.objects.filter(estado=True)
        datos = {'no_barrios': no_barrios, 'barrios': barrios}
        return render(request,'barrio/crudBarrio.html', datos)
    else:
        return redirect('exit')
@login_required
def crearBarrio(request):
    if request.user.tipo.id == 1:
        if request.method == 'POST':
            formaBarrio = FormBarrio(request.POST)
            if formaBarrio.is_valid():
                formaBarrio.save()
                return redirect('crudBarrio')
        else:
            formaBarrio = FormBarrio()
        datos = {'formaBarrio': formaBarrio}
        return render(request, 'barrio/crearBarrio.html', datos)
    else:
        return redirect('exit')
@login_required
def editarBarrio(request,id):
    if request.user.tipo.id == 1:
        barrio = get_object_or_404(Barrio, pk=id)
        if request.method == 'POST':
            formaBarrio = FormBarrio(request.POST, instance=barrio)
            if formaBarrio.is_valid():
                formaBarrio.save()
                return redirect('crudBarrio')
        else:
            formaBarrio = FormBarrio(instance=barrio)
        datos = {'formaBarrio': formaBarrio}
        return render(request, 'barrio/editarBarrio.html', datos)
    else:
        return redirect('exit')

@login_required
def eliminarBarrio(request,id):
    if request.user.tipo.id == 1:
        barrio = get_object_or_404(Barrio, pk=id)
        if barrio:
            barrio.estado = False
            barrio.save()
        return redirect('crudBarrio')
    else:
        return redirect('exit')

@login_required
def crudEstablecimiento(request):
    if request.user.tipo.id == 1:
        no_establecimientos = Establecimiento.objects.filter(estado=True).count()
        establecimientos = Establecimiento.objects.filter(estado=True)
        datos = {'no_establecimientos': no_establecimientos, 'establecimientos': establecimientos}
        return render(request,'establecimiento/crudEstablecimiento.html',datos)
    else:
        return redirect('exit')


@login_required
def crearEstablecimiento(request):
    if request.user.tipo.id == 1:
        if request.method == 'POST':
            formaEstablecimiento = FormEstablecimiento(request.POST)
            if formaEstablecimiento.is_valid():
                formaEstablecimiento.save()
                return redirect('crudEstablecimiento')
        else:
            formaEstablecimiento = FormEstablecimiento()
        datos = {'formaEstablecimiento': formaEstablecimiento}
        return render(request,'establecimiento/crearEstablecimiento.html', datos)
    else:
        return redirect('exit')

@login_required
def editarEstablecimiento(request,id):
    if request.user.tipo.id == 1:
        establecimiento = get_object_or_404(Establecimiento, pk=id)
        if request.method == 'POST':
            formaEstablecimiento = FormEstablecimiento(request.POST, instance=establecimiento)
            if formaEstablecimiento.is_valid():
                formaEstablecimiento.save()
                return redirect('crudEstablecimiento')
        else:
            formaEstablecimiento = FormEstablecimiento(instance=establecimiento)
        datos = {'formaEstablecimiento': formaEstablecimiento}
        return render(request, 'establecimiento/editarEstablecimiento.html', datos)
    else:
        return redirect('exit')

@login_required
def eliminarEstablecimiento(request,id):
    if request.user.tipo.id == 1:
        establecimiento = get_object_or_404(Establecimiento, pk=id)
        if establecimiento:
            establecimiento.estado = False
            establecimiento.save()
        return redirect('crudEstablecimiento')
    else:
        return redirect('exit')


@login_required
def vistaAdmin(request):
    if request.user.tipo.id == 1:
        return render(request,'vistaAdmin.html')
    else:
        return redirect('exit')
@login_required
def vistaTes(request):
    if request.user.tipo.id == 2:
        if request.method == 'POST':
            formaPago = FormPago2(request.POST)
            if formaPago.is_valid():
                formaPago.save()
                return redirect('vistaTes')
        else:
            formaPago = FormPago2()
        datos = {'formaPago': formaPago}
        return render(request, 'vistaTes.html', datos)
    else:
        return redirect('exit')

@login_required
def hisPagos(request):
    if request.user.tipo.id == 2:
        no_pagos = Pagos.objects.filter(estado=True).count()
        pagos = Pagos.objects.filter(estado=True)
        totalPagos = Pagos.objects.aggregate(total=Sum('monto'))['total']
        datos = {'no_pagos': no_pagos, 'pagos': pagos, 'totalPagos': totalPagos}
        return render(request, 'pagos/hisPagos.html', datos)
    else:
        return redirect('exit')


@login_required
def crudPagos(request):
    if request.user.tipo.id == 1:
        no_pagos = Pagos.objects.filter(estado=True).count()
        pagos = Pagos.objects.filter(estado=True)
        datos = {'no_pagos': no_pagos, 'pagos': pagos}
        return render(request, 'pagos/crudPagos.html', datos)
    else:
        return redirect('exit')

@login_required
def editarPagos(request,id):
    if request.user.tipo.id == 1:
        pago = get_object_or_404(Pagos, pk=id)
        if request.method == 'POST':
            formaPago = FormPago(request.POST, instance=pago)
            if formaPago.is_valid():
                formaPago.save()
                return redirect('crudPagos')
        else:
            formaPago = FormPago(instance=pago)
        datos = {'formaPago': formaPago}
        return render(request, 'pagos/editarPagos.html', datos)
    else:
        return redirect('exit')

@login_required
def eliminarPagos(request,id):
    if request.user.tipo.id == 1:
        pago = get_object_or_404(Pagos, pk=id)
        if pago:
            pago.estado = False
            pago.save()
        return redirect('crudPagos')
    else:
        return redirect('exit')

@login_required
def vistaRec(request):
    if request.user.tipo.id == 3:
        if request.method == 'GET':
            id_busqueda = request.GET.get('id_busqueda')
            if id_busqueda:
                cuenta_buscada = Cuenta.objects.filter(id=id_busqueda,estado=True).first()
                if cuenta_buscada:
                    id = cuenta_buscada.id
                    return redirect('detallesRecaudo',id)
                else:
                    error_message = 'No se encontró ninguna cuenta con el ID proporcionado.'
                    return render(request, 'vistaRec.html', {'error_message': error_message})
            else:
                error_message = 'Debe ingresar una ID para buscar una cuenta.'
                return render(request, 'vistaRec.html', {'error_message': error_message})
        return render(request,'vistaRec.html')
    else:
        return redirect('exit')
@login_required
def detallesRecaudo(request,id):
    if request.user.tipo.id == 3:
        cuenta_buscada = get_object_or_404(Cuenta, pk=id)
        datos = {'cuenta_buscada': cuenta_buscada}
        return render(request,'recaudos/detallesRecaudo.html', datos)
    else:
        redirect('exit')

@login_required
def generarRecaudo(request, id):
    if request.user.tipo.id == 3:
        cuenta_buscada = get_object_or_404(Cuenta, pk=id)
        if request.method == 'POST':
            saldo_ingresado = int(request.POST.get('saldo'))
            print(saldo_ingresado)

            factura = Recaudos()
            factura.id_cuenta = cuenta_buscada
            factura.monto = saldo_ingresado
            factura.save()
            cuenta_buscada.saldo = cuenta_buscada.saldo - saldo_ingresado
            cuenta_buscada.save()
            return redirect('vistaRec')

        datos = {'cuenta_buscada': cuenta_buscada}
        return render(request, 'recaudos/generarRecaudo.html', datos)
    else:
        return redirect('exit')

@login_required
def crudRecaudos(request):
    if request.user.tipo.id == 1:
        no_recaudos = Recaudos.objects.filter(estado=True).count()
        recaudos = Recaudos.objects.filter(estado=True)
        datos = {'no_recaudos': no_recaudos, 'recaudos': recaudos}
        return render(request,'recaudos/crudRecaudos.html',datos)
    else:
        return redirect('exit')

@login_required
def eliminarRecaudos(request,id):
    if request.user.tipo.id == 1:
        recaudo = get_object_or_404(Recaudos, pk=id)
        if recaudo:
            recaudo.estado = False
            recaudo.save()
        return redirect('crudRecaudo')
    else:
        return redirect('exit')

@login_required
def crudUsuario(request):
    if request.user.tipo.id == 1:
        no_usuarios = User.objects.filter(is_superuser=True, is_staff=True).count()
        usuarios = User.objects.filter(is_superuser=True, is_staff=True)
        datos = {'no_usuarios': no_usuarios, 'usuarios': usuarios}
        return render(request,'usuarios/crudUsuario.html',datos)
    else:
        return redirect('exit')

@login_required
def crearUsuario(request):
    if request.user.tipo.id == 1:
        if request.method == 'POST':
            formaUsuario = FormUser(request.POST)
            if formaUsuario.is_valid():
                username = formaUsuario.cleaned_data['username']
                first_name = formaUsuario.cleaned_data['first_name']
                last_name = formaUsuario.cleaned_data['last_name']
                email = formaUsuario.cleaned_data['email']
                password = formaUsuario.cleaned_data['password']
                tipo = formaUsuario.cleaned_data['tipo']
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password, tipo=tipo)
                user.is_superuser = True
                user.is_staff = True
                user.save()
                return redirect('crudUsuario')
        else:
            formaUsuario = FormUser
        datos = {'formaUsuario': formaUsuario}
        return render(request,'usuarios/crearUsuario.html',datos)
    else:
        return redirect('exit')

@login_required
def editarUsuario(request,id):
    if request.user.tipo.id == 1:
        usuario = get_object_or_404(User, pk=id)
        if request.method == 'POST':
            formaUsuario = FormUser(request.POST, instance=usuario)
            if formaUsuario.is_valid():
                formaUsuario.save()
                return redirect('crudUsuario')
        else:
            formaUsuario = FormUser(instance=usuario)
        datos = {'formaUsuario': formaUsuario}
        return render(request,'usuarios/editarUsuario.html',datos)
    else:
        return redirect('exit')

@login_required
def eliminarUsuario(request,id):
    if request.user.tipo.id == 1:
        usuario = get_object_or_404(User, pk=id)
        if usuario:
            usuario.is_superuser = False
            usuario.is_staff = False
            usuario.is_active = False
            usuario.save()
        return redirect('crudUsuario')
    else:
        return redirect('exit')

