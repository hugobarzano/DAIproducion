from django.http import HttpResponse
from django.shortcuts import render
from bares_y_tapas.models import *
from bares_y_tapas.forms import *
from django.http import JsonResponse

def index(request):
	#contexto para enviar al motor de plantillas
	top_bares = Bar.objects.order_by('-visitas')[:5]
	top_tapas = Tapa.objects.order_by('-megusta')[:5]
	#print top_tapas
	contexto = {'Bares': top_bares, 'Tapas': top_tapas}
	#Renderizamos la respuesta para el cliente
	return render(request, 'bares_y_tapas/index.html', contexto)

def todos(request):
	#contexto para enviar al motor de plantillas
	bares = Bar.objects.all()
	contexto = {'Bares': bares}
	#Renderizamos la respuesta para el cliente
	return render(request, 'bares_y_tapas/todos.html', contexto)

def about(request):
	return render(request, 'bares_y_tapas/about.html')

def details(request,nombre_bar):
	bar_detalle = Bar.objects.get(nombre=nombre_bar)
	#print bar_detalle
	#contexto ={'Bar': bar_detalle}
	#lista_tapas=Tapa.objects.order_by('-megusta')[:5]
	lista_tapas=Tapa.objects.filter(bar=bar_detalle)
	#print lista_tapas
	contexto={ 'Bar': bar_detalle, 'Tapas' : lista_tapas}
	#print contexto
	return render(request, 'bares_y_tapas/details.html', contexto)

def bar(request, bar_nombre_slug):
	contexto = {}
	try:
		bar = Bar.objects.get(slug=bar_nombre_slug)
		Bar.objects.filter(slug=bar_nombre_slug).update(visitas=bar.visitas+1)

		#bar = Bar.objects.get(slug=bar_nombre_slug)
		contexto['bar_nombre'] = bar.nombre

		tapas = Tapa.objects.filter(bar=bar)
		contexto['tapas'] = tapas
		contexto['bar']=bar
		contexto['bar_nombre_slug']=bar_nombre_slug
	except Bar.DoesNotExist:
		pass

	return render(request,'bares_y_tapas/bar.html', contexto)


def add_bar(request):
    if request.method == 'POST':
        form = BarForm(request.POST)

        if form.is_valid():
			form.save(commit=True)
			return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = BarForm()

    return render(request, 'bares_y_tapas/add_bar.html', {'form': form})

def add_tapa(request, bar_nombre_slug):

    try:
        bar = Bar.objects.get(slug=bar_nombre_slug)
    except Bar.DoesNotExist:
                bar = None

    if request.method == 'POST':
        form = TapaForm(request.POST)
        if form.is_valid():
            if bar:
				contexto = {}
				tapa = form.save(commit=False)
				tapa.bar = bar
				tapa.megusta = 0
				tapa.save()
				contexto['bar_nombre'] = bar.nombre
				tapas = Tapa.objects.filter(bar=bar)
				contexto['tapas'] = tapas
				contexto['bar']=bar
				contexto['bar_nombre_slug']=bar_nombre_slug
				return render(request,'bares_y_tapas/bar.html', contexto)

        else:
            print form.errors
    else:
        form = TapaForm()

    context_dict = {'form':form, 'bar': bar,'bar_nombre_slug':bar_nombre_slug}

    return render(request, 'bares_y_tapas/add_tapa.html', context_dict)


def reclama_datos (request):
	bares = Bar.objects.order_by('-visitas')[:5]
	datos = {}
	#for b in bares:
	#	datos={'nombre_bares':b.nombre,'visitas_bares':b.visitas}
	datos={'nombre_bares':[bares[0].nombre,bares[1].nombre,bares[2].nombre,bares[3].nombre,bares[4].nombre],
		'visitas_bares':[bares[0].visitas,bares[1].visitas,bares[2].visitas,bares[3].visitas,bares[4].visitas]}
	print (datos)
	#for b in bares:
		#datos[b.nombre]=b.visitas

	return JsonResponse(datos, safe=False)
