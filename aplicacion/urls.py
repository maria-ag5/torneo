from django.urls import path
from aplicacion import views

urlpatterns = [
    path('', views.menu_view, name='menu_view'),
    path('torneo/', views.torneo, name='torneo'),
    path('tabla/', views.tabla, name='tabla'),
    path('campeon/', views.campeon, name='campeon'),
    path('inicio/', views.inicio, name='inicio'),
]