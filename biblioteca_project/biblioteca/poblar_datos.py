from biblioteca.models import Autor, Libro, Resena

# Crear autores
autor1 = Autor.objects.create(nombre="Gabriel García Márquez", nacionalidad="Colombiana")
autor2 = Autor.objects.create(nombre="Isabel Allende", nacionalidad="Chilena")

# Crear libros
libro1 = Libro.objects.create(titulo="Cien años de soledad", resumen="Una historia épica sobre la familia Buendía en Macondo...", autor=autor1)
libro2 = Libro.objects.create(titulo="La casa de los espíritus", resumen="Saga familiar que mezcla realismo mágico y drama...", autor=autor2)

# Crear reseñas
Resena.objects.create(libro=libro1, texto="Obra maestra del realismo mágico.", calificacion=5)
Resena.objects.create(libro=libro2, texto="Muy emocionante y profunda.", calificacion=4)

print("✅ Datos cargados exitosamente.")
