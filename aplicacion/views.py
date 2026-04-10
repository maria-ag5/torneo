from django.shortcuts import render, redirect

def inicio(request):
    if request.method == "POST":
        user=request.POST.get("username")
        password=request.POST.get("password")
    
        if user== "cosita" and password == "1234":
            return redirect("home")
        else:
            return render(request, "inicio.html", {"error": "Datos incorrectos"})

    return render(request, "inicio.html")

