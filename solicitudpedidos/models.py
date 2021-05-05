from django.db import models

# Create your models here.


class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(
        self,
    ):
        return "%s %s, sector: %s, email: %s" % (
            self.nombre,
            self.apellido,
            self.sector,
            self.email,
        )