from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login_usuarios(
    request,
):
    return render(request, "solicitudpedidos/login.html")


def formulario_pedidos(
    request,
):
    return render(request, "solicitudpedidos/formulario_pedidos.html")
