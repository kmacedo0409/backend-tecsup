
# aCA DEFINIREMOS TODAS LAS RUTAS QUE TENDRA ACCESO A NUESTRA APLICACION
from django.urls import path
from .views import DepartamentosApiView, saludar, parametros, PruebaApiView, DepartamentoApiView

# Tenemos que crear esta variable NO SE PUEDE LLAMAR DE OTRA MANERA

urlpatterns=[
    path('inicio/', saludar),
    path('parametros/<str:nombre>', parametros),
    path('prueba/', PruebaApiView.as_view()),
    path('departamentos/', DepartamentosApiView.as_view()),
    path('departamento/<int:pk>', DepartamentoApiView.as_view()),
]