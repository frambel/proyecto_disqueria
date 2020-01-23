from django.db import models

class Disco(models.Model):
    titulo = models.CharField(max_length=200)
    disquera = models.ForeignKey('Disquera', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default='')
    precio = models.FloatField()
    def __str__(self):
        return self.titulo

class Artista(models.Model):
    nombre = models.CharField(max_length=200)
    disco = models.ManyToManyField('Disco')
    pais = models.ForeignKey('Pais', on_delete=models.DO_NOTHING)
    mail = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre

class Disquera(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    sitioweb = models.URLField()
    def __str__(self):
        return self.nombre  


class Genero(models.Model):
    nombre = models.CharField(max_length=200)
    disco =models.ManyToManyField(Disco)

    def __str__(self):
        return self.nombre


class Pais(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre