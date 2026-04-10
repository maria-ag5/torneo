from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu_view'),
    path('torneo/', views.torneo, name='torneo'),
    path('tabla/', views.tabla, name='tabla'),
    path('campeon/', views.campeon, name='campeon'),
=======
from .views import inicio

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
>>>>>>> d74089540be8f8301c65ae446efadbb645286941
]