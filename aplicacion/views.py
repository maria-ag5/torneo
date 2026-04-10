from django.shortcuts import render

def menu_view(request):
    return render(request, 'menu.html')
# equipos del torneo
equipos = ["PSG", "Bayer", "Athletic", "Chelsea"]

# generar partidos una sola vez
partidos = []

for i in range(len(equipos)):
    for j in range(i + 1, len(equipos)):
        partidos.append({
            "equipoA": equipos[i],
            "equipoB": equipos[j],
            "golesA": "",
            "golesB": ""
        })


# vista para registrar resultados
def torneo(request):

    if request.method == "POST":
        index = int(request.POST["index"])
        golesA = request.POST["golesA"]
        golesB = request.POST["golesB"]

        partidos[index]["golesA"] = golesA
        partidos[index]["golesB"] = golesB

    return render(request, "aplicacion/torneo.html", {"partidos": partidos})


# vista para mostrar tabla de posiciones
def tabla(request):

    tabla = {}

    # inicializar tabla
    for equipo in equipos:
        tabla[equipo] = {
            "pj": 0,
            "pg": 0,
            "pe": 0,
            "pp": 0,
            "pts": 0
        }

    # recorrer partidos jugados
    for p in partidos:

        if p["golesA"] == "" or p["golesB"] == "":
            continue

        golesA = int(p["golesA"])
        golesB = int(p["golesB"])

        equipoA = p["equipoA"]
        equipoB = p["equipoB"]

        tabla[equipoA]["pj"] += 1
        tabla[equipoB]["pj"] += 1

        if golesA > golesB:
            tabla[equipoA]["pg"] += 1
            tabla[equipoA]["pts"] += 3
            tabla[equipoB]["pp"] += 1

        elif golesB > golesA:
            tabla[equipoB]["pg"] += 1
            tabla[equipoB]["pts"] += 3
            tabla[equipoA]["pp"] += 1

        else:
            tabla[equipoA]["pe"] += 1
            tabla[equipoB]["pe"] += 1
            tabla[equipoA]["pts"] += 1
            tabla[equipoB]["pts"] += 1

    return render(request,"aplicacion/tabla.html",{"tabla":tabla})
