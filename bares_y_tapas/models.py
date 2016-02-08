from django.db import models
from django.template.defaultfilters import slugify

class Bar(models.Model):
    nombre=models.CharField(max_length=128, unique=True)
    direccion=models.CharField(max_length=256)
    visitas = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Bar, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre

class Tapa(models.Model):
    bar=models.ForeignKey(Bar)
    nombre_tapa = models.CharField(max_length=128)
    megusta = models.IntegerField(default=0)

    def __unicode__(self):
        return self.nombre_tapa
