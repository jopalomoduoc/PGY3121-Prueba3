from django.db import models

# Create your models here.
#ISBN
# Nombre del libro 
# Autor 
# Descripción 
# Categoría: cada registro debe estar asociado a una categoría. 
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name ="Nombre de la categoria")

    def __str__(self):
        return self.nombreCategoria

class Libro(models.Model):
    ISBN = models.CharField(max_length=13, primary_key=True, verbose_name='Codigo')
    nombreLibro = models.CharField(max_length=255, verbose_name='Nombre del libro')
    descripcion = models.CharField(max_length=255, null=True, blank=True, verbose_name='Descripcion')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.ISBN        
