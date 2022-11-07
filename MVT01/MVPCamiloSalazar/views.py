from django.http import HttpResponse
from django.template import Template, Context

from datetime import datetime







def MVT01(request):

    # Abrimos el archivo
    archivo = open(r"C:/Users/Csala/OneDrive/Escritorio/CODER HOUSE/MVTCamiloSalazar/MVT01/MVPCamiloSalazar/templates/MVT_CamiloSalazar.html")

    # Creamos el template
    plantilla = Template(archivo.read())
    # Cerramos el archivo para liberar recursos
    
    archivo.close()

    # Creamos el diccionario de datos
    listado_familia = ["Maria Eugenia", "Sergio Alfredo", "Constanza Javiera", "Maria Carolina", "Camilo Salazar"]

    datos = {'fecha':datetime.now(),'nombre': 'CODERHOUSE LOVER!!!',"Integrantes": "Familia Salazar Fuentes", "listado_familia": listado_familia }

    # Creamos el contexto
    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)