from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu_view'),
    path('torneo/', views.torneo, name='torneo'),
    path('tabla/', views.tabla, name='tabla'),
]