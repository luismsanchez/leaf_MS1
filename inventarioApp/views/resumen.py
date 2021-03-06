from rest_framework import generics
from django.contrib.auth.models import User
from ..models import Proveedor, Producto, Cliente, Comentario
from ..serializers import ProductoSerializer, ComentarioSerializer, ClienteSerializer, ProveedorSerializer, UserSerializer

# Resumen

class ComentariosDeProductoList(generics.ListAPIView):
    serializer_class = ComentarioSerializer

    def get(self, request, *args, **kwargs):
        producto = Producto.objects.get(pk=kwargs['pk'])
        self.queryset = Comentario.objects.filter(producto=producto).order_by("-creacion",'-calificacion')
        return self.list(request, *args, **kwargs)


class ComentariosDeClienteList(generics.ListAPIView):
    serializer_class = ComentarioSerializer

    def get(self, request, *args, **kwargs):
        cliente = Cliente.objects.get(pk=kwargs['pk'])
        self.queryset = Comentario.objects.filter(cliente=cliente).order_by("-creacion", '-calificacion')
        return self.list(request, *args, **kwargs)


class ProductosDeProveedorList(generics.ListAPIView):
    serializer_class = ProductoSerializer

    def get(self, request, *args, **kwargs):
        proveedor = Proveedor.objects.get(pk=kwargs['pk'])
        self.queryset = Producto.objects.filter(proveedor=proveedor).order_by('nombre')
        return self.list(request, *args, **kwargs)


class ClientesDeUserList(generics.ListAPIView):
    serializer_class = ClienteSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        self.queryset = Cliente.objects.filter(user=user).order_by('nombre')
        return self.list(request, *args, **kwargs)


class ProveedoresDeUserList(generics.ListAPIView):
    serializer_class = ProveedorSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        self.queryset = Proveedor.objects.filter(user=user).order_by('nombre')
        return self.list(request, *args, **kwargs)