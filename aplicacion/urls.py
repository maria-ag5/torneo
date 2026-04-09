from django.urls import path
from . import views

urlpatterns = [
    path('torneo/', views.torneo, name='torneo'),
    path('tabla/', views.tabla, name='tabla'),
]