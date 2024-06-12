from django.db import models

# Create your models here.

class ViajerosResidenciaDestino(models.Model):
    indice_tiempo = models.DateField(blank=False)
    region_de_destino = models.CharField(max_length=25, blank=False)
    origen_viajeros = models.CharField(max_length=25, blank=False)
    viajeros = models.IntegerField(default=0)
    observaciones = models.TextField(blank=True)

    class Meta:
        ordering = ['indice_tiempo', 'region_de_destino']


    def __str__(self):
        return str(self.indice_tiempo)+', '+str(self.region_de_destino)+', '+str(self.origen_viajeros)+', '+str(self.viajeros)

