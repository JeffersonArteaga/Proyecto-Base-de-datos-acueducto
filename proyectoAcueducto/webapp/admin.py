from django.contrib import admin


from webapp.models import Cliente, Cuenta, Establecimiento, Barrio, Pagos, Recaudos

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Cuenta)
admin.site.register(Establecimiento)
admin.site.register(Barrio)
admin.site.register(Pagos)
admin.site.register(Recaudos)
