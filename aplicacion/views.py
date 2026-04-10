from django.shortcuts import render, redirect
from .models import Equipo, Partido
from django.db.models import Q
import itertools
import random


def torneo(request):

    # Reiniciar torneo
    if request.method == "POST" and request.POST.get("reset"):
        Partido.objects.all().delete()
        return redirect("torneo")

    equipos = list(Equipo.objects.all())

    # Crear partidos si no existen
    if Partido.objects.count() == 0:

        combinaciones = list(itertools.combinations(equipos, 2))
        random.shuffle(combinaciones)

        for a, b in combinaciones:
            Partido.objects.create(
                equipo_a=a,
                equipo_b=b,
                goles_a=0,
                goles_b=0,
                jugado=False
            )

    # Guardar resultado de un partido
    if request.method == "POST" and request.POST.get("partido_id"):

        partido_id = request.POST.get("partido_id")
        goles_a = request.POST.get("goles_a")
        goles_b = request.POST.get("goles_b")

        partido = Partido.objects.get(id=partido_id)

        # Solo guardar si aún no se ha jugado
        if not partido.jugado:
            partido.goles_a = int(goles_a)
            partido.goles_b = int(goles_b)
            partido.jugado = True
            partido.save()

        return redirect("torneo")

    partidos = Partido.objects.all()

    return render(request, "aplicacion/torneo.html", {
        "partidos": partidos
    })


def tabla(request):

    equipos = Equipo.objects.all()
    tabla = []

    for equipo in equipos:

        pj = 0
        pg = 0
        pe = 0
        pp = 0
        pts = 0

        partidos = Partido.objects.filter(
            Q(equipo_a=equipo) | Q(equipo_b=equipo),
            jugado=True
        )

        for p in partidos:

            pj += 1

            if p.goles_a == p.goles_b:
                pe += 1
                pts += 1

            elif p.equipo_a == equipo and p.goles_a > p.goles_b:
                pg += 1
                pts += 3

            elif p.equipo_b == equipo and p.goles_b > p.goles_a:
                pg += 1
                pts += 3

            else:
                pp += 1

        tabla.append({
            "equipo": equipo.nombre,
            "pj": pj,
            "pg": pg,
            "pe": pe,
            "pp": pp,
            "pts": pts
        })

    tabla = sorted(tabla, key=lambda x: x["pts"], reverse=True)

    return render(request, "aplicacion/tabla.html", {
        "tabla": tabla
    })

def campeon(request):

    equipos = Equipo.objects.all()
    tabla = []

    for equipo in equipos:

        pj = pg = pe = pp = pts = 0

        partidos = Partido.objects.filter(
            Q(equipo_a=equipo) | Q(equipo_b=equipo),
            jugado=True
        )

        for p in partidos:

            pj += 1

            if p.goles_a == p.goles_b:
                pe += 1
                pts += 1

            elif p.equipo_a == equipo and p.goles_a > p.goles_b:
                pg += 1
                pts += 3

            elif p.equipo_b == equipo and p.goles_b > p.goles_a:
                pg += 1
                pts += 3

            else:
                pp += 1

        tabla.append({
            "equipo": equipo.nombre,
            "pts": pts
        })

    tabla = sorted(tabla, key=lambda x: x["pts"], reverse=True)

    return render(request,"aplicacion/campeon.html",{
        "tabla": tabla
    })