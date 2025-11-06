from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Autor, Libro, Resena
from .serializers import AutorSerializer, LibroSerializer, ResenaSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['autor']
    ordering_fields = ['anio', 'titulo']

    @action(detail=True, methods=['get'])
    def promedio_rating(self, request, pk=None):
        libro = self.get_object()
        reseñas = libro.resenas.all()
        if reseñas.exists():
            promedio = sum(r.rating for r in reseñas) / reseñas.count()
        else:
            promedio = 0
        return Response({'libro': libro.titulo, 'promedio_rating': promedio})


class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all().order_by('-fecha')
    serializer_class = ResenaSerializer

    def perform_create(self, serializer):
        print("Creando una nueva reseña...")
        serializer.save()
