from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Partido(models.Model):
    equipo_a = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='equipo_a')
    equipo_b = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='equipo_b')
    goles_a = models.IntegerField(default=0)
    goles_b = models.IntegerField(default=0)
    jugado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.equipo_a} vs {self.equipo_b}"


class Tabla(models.Model):
    equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE)
    jugados = models.IntegerField(default=0)
    ganados = models.IntegerField(default=0)
    empatados = models.IntegerField(default=0)
    perdidos = models.IntegerField(default=0)
    puntos = models.IntegerField(default=0)

    def __str__(self):
        return self.equipo.nombre
