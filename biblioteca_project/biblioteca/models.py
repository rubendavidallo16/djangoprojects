from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

def validar_nombre_autor(nombre):
    if not nombre.strip():
        raise ValidationError("El nombre del autor no puede estar vacío o solo tener espacios.")

def validar_resumen(resumen):
    if len(resumen) < 50:
        raise ValidationError("El resumen debe tener al menos 50 caracteres.")


class Autor(models.Model):
    nombre = models.CharField(max_length=100, validators=[validar_nombre_autor])
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    resumen = models.TextField(validators=[validar_resumen])
    anio = models.PositiveIntegerField(default=2000)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')

    def __str__(self):
        return self.titulo


class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    texto = models.TextField()
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.libro.titulo} ({self.rating}/5)"
