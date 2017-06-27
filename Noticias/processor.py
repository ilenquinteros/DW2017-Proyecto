from AdminCuentas.models import Categoria

def categoriasMenu(request):
    return {'categoriasMenu': Categoria.objects.all()}