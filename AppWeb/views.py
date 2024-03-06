from django.shortcuts import render
from django.http import HttpResponse
from AppWeb.models import Empleado, Vacante, Departamento
from AppWeb.forms import FormularioEmpleado, FormularioDepartamento

# Create your views here.

def inicio(request):


    return render(request, 'inicio.html')


def ver_empleado(request):

    return render(request, "ver_empleado.html")

def ver_vacante(request):

    return render(request, "ver_vacante.html")

def ver_departamento(request):

    return render(request, "ver_departamento.html")


def crear_vacante(request):

    if request.method == "POST": #Cuando aprieto el boton de enviar!!!
        
        vacante_nueva = Vacante(titulo=request.POST["titulo"],descripcion=request.POST["descripcion"],requisitos= request.POST["requisitos"],salario=request.POST["salario"])
        #Leer la informacion y guardarla en la base de datos!!!
        vacante_nueva.save()

        return render(request, "inicio.html")

    
    return render(request, "crear_vacante.html")

    
def crear_empleado(request):

    if request.method == "POST":

        formulario = FormularioEmpleado(request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            empleado_nuevo = Empleado(
                nombre=info_dic["nombre"],
                apellido=info_dic["apellido"],
                puesto=info_dic["puesto"],
                salario=info_dic["salario"],
                )
            
            empleado_nuevo.save()

            return render(request, "inicio.html")
        
    else:

        formulario = FormularioEmpleado()

    return render(request, "crear_empleado.html", {"formu":formulario})



def crear_departamento(request):

    if request.method == "POST":

        formulario = FormularioDepartamento(request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            departamento_nuevo = Departamento(
                nombre=info_dic["nombre"],
                descripcion=info_dic["descripcion"],

                )
            
            departamento_nuevo.save()

            return render(request, "inicio.html")
        
    else:

        formulario = FormularioDepartamento()

    return render(request, "crear_departamento.html", {"formu_departamento":formulario}) 




def buscar_vacante(request):
    

    if request.GET: #Solo si es que hay una busqueda!!!

        nombre = request.GET["titulo"]  #leer el diccionario de info del formulario y obtengo el valor de busqueda
        requisitos= Vacante.objects.filter(nombre__icontains=nombre) 
        
        mensaje = f"Estamos buscando al departamento {nombre}"

        return render(request, "resultados_vacante.html", {"mensaje":mensaje, "resultados":requisitos})

    
    return render(request, "resultados_vacante.html") #si todavia no hay una busqueda



