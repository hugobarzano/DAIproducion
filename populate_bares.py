import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practica4.settings')
from bares_y_tapas.models import *
import django
django.setup()



def populate():
    stukas_bar = add_bar('Stukas','Calle Pedro Antonio de Alarcon 1',400)
    add_tapa(bar=stukas_bar,
        nombre="Jarra medio litro",
        megusta=95)
    add_tapa(bar=stukas_bar,
        nombre="Jarra Sparten litro",
        megusta=12)
    add_tapa(bar=stukas_bar,
        nombre="Voll-Damm",
        megusta=666)

    perro_bar = add_bar('Perro Andaluz','Calle Pedro Antonio de Alarcon 2',500)
    add_tapa(bar=perro_bar,
        nombre="Jarra medio litro",
        megusta=70)
    add_tapa(bar=perro_bar,
        nombre="calimocho",
        megusta=34)
    add_tapa(bar=perro_bar,
        nombre="Jarra + perrito",
        megusta=75)

    lobo_bar = add_bar('La Guarida del Lobo','Calle Pedro Antonio de Alarcon 3',200)
    add_tapa(bar=lobo_bar,
        nombre="Jarra medio litro",
        megusta=45)
    add_tapa(bar=lobo_bar,
        nombre="Chupito Absenta",
        megusta=666)
    add_tapa(bar=lobo_bar,
        nombre="Budweiser",
        megusta=75)

    deltoya_bar = add_bar('Deltoya','Calle Pedro Antonio de Alarcon 4',100)
    add_tapa(bar=deltoya_bar,
        nombre="Jarra medio litro",
        megusta=100)
    add_tapa(bar=deltoya_bar,
        nombre="Chupito Absenta",
        megusta=666)
    add_tapa(bar=deltoya_bar,
        nombre="Chupito Jagermeister",
        megusta=75)

    rainbow_bar = add_bar('Rainbow','Calle Pedro Antonio de Alarcon 5',150)
    add_tapa(bar=rainbow_bar,
        nombre="Jarra medio litro",
        megusta=140)
    add_tapa(bar=rainbow_bar,
        nombre="Cerveza negra",
        megusta=123)
    add_tapa(bar=rainbow_bar,
        nombre="Tercio Alhambra",
        megusta=75)

    tren_bar = add_bar('Sala El Tren','Ctra. de Malaga',6000)
    add_tapa(bar=tren_bar,
        nombre="Jarra medio litro",
        megusta=600)
    add_tapa(bar=tren_bar,
        nombre="Tercio Alhambra",
        megusta=123)
    add_tapa(bar=tren_bar,
        nombre="Cubalibre Nacional",
        megusta=125)
    add_tapa(bar=tren_bar,
        nombre="Cubalibre Importacion",
        megusta=225)

    for b in Bar.objects.all():
        for t in Tapa.objects.filter(bar=b):
            print "- {0} - {1}".format(str(b), str(t))


def add_tapa(bar, nombre, megusta):
    t = Tapa.objects.get_or_create(bar=bar, nombre_tapa=nombre)[0]
    t.nombre_tapa=nombre
    t.megusta=megusta
    t.save()
    return t

def add_bar(nombre,direccion,visitas):
    b = Bar.objects.get_or_create(nombre=nombre,direccion=direccion,visitas=visitas)[0]
    return b



if __name__ == '__main__':
    print "Starting bares population script..."
    populate()
