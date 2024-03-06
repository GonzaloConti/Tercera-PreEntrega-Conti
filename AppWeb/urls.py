from django.urls import path
from AppWeb import views

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('crearEmpleado', views.crear_empleado, name='crear_empleado'),
    path('crearDepartamento', views.crear_departamento, name='crear_departamento'),
    path('crearVacante', views.crear_vacante, name='crear_vacante'),
    
    path('verEmpleado', views.ver_empleado, name='ver_empleado'),
    path('verDepartamento', views.ver_departamento, name='ver_departamento'),
    path('verVacante', views.ver_vacante, name='ver_vacante'),
    
    path("buscar_vacante/", views.buscar_vacante),

    
    
    
]