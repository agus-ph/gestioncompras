from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def login_usuarios(
    request,
):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("formulario_pedidos")
        else:
            messages.info(request, "usuario o contraseña incorrectos")
    context = {}
    return render(request, "solicitudpedidos/login.html", context)


def formulario_pedidos(
    request,
):
    return render(request, "solicitudpedidos/formulario_pedidos.html")
