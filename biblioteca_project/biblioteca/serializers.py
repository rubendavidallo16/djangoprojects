from rest_framework import serializers
from .models import Autor, Libro, Resena

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '__all__'


class LibroSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='autor.nombre')
    recent_reviews = serializers.SerializerMethodField()

    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'resumen', 'anio', 'autor', 'author_name', 'recent_reviews']

    def get_recent_reviews(self, obj):
        reseñas = obj.resenas.order_by('-fecha')[:5]
        return ResenaSerializer(reseñas, many=True).data
