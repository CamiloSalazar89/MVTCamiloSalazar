from django.http import HttpResponse
from appcoder.models import Familia

# Create your views here.

def listado_familia(request):
    Familia = Grupo.objects.all()

    cadena_respuesta = ''
    for Grupo in Familia:
        cadena_respuesta += Grupo.Familia + ' | '

        return HttpResponse(cadena_respuesta)
        pass
        pass