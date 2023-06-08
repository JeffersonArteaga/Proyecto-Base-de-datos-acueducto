from django import forms
from django.forms import ModelForm
from webapp.models import Cliente, Establecimiento, Barrio, Cuenta, Pagos


class FormCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {

        }

class FormEstablecimiento(ModelForm):
    class Meta:
        model = Establecimiento
        fields = '__all__'
        widgets = {

        }

class FormBarrio(ModelForm):
    class Meta:
        model = Barrio
        fields = '__all__'
        widgets = {

        }

class FormCuenta(ModelForm):
    class Meta:
        model = Cuenta
        fields = '__all__'
        widgets = {

        }

    def clean_saldo(self):
        saldo = self.cleaned_data['saldo']
        if saldo < 0:
            raise forms.ValidationError("El saldo no puede ser menor a cero")
        return saldo

class FormPago(ModelForm):
    class Meta:
        model = Pagos
        fields = '__all__'
        widgets = {

        }

    def clean_monto(self):
        monto = self.cleaned_data['monto']
        if monto < 0:
            raise forms.ValidationError("El monto no puede ser menor a cero")
        return monto

class FormPago2(ModelForm):
    class Meta:
        model = Pagos
        fields = ('descripcion', 'monto')
        widgets = {

        }

    def clean_monto(self):
        monto = self.cleaned_data['monto']
        if monto < 0:
            raise forms.ValidationError("El monto no puede ser menor a cero")
        return monto