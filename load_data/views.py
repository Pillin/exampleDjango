from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from load_data.models import Stock

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def load_csv(request):
    return render_to_response("load_csv.html", context_instance = RequestContext(request))


def load_csv_post(request):
    filename = request.FILES['file'].name
    data = request.FILES['file'].read()
    if  filename.split(".")[-1].lower() != "csv" or not len(data):
        return render_to_response("load_csv.html", {"messages": "error en la subida de archivos"}, context_instance = RequestContext(request))
    
    processing_file(data)

    return render_to_response("load_csv.html", {"messages": "Archivo subido correctamente"}, context_instance = RequestContext(request))


def processing_file(data):
    info = data.splitlines(True)
    info.pop(0)
    for row in info:
        lista = row.split(";")
        try:
            stock_prod = Stock.objects.get(id_stock=int(lista[4]))
        except:
            stock_prod = Stock()
        stock_prod.cod_local = lista[0]
        stock_prod.cod_mat = int(lista[1])
        stock_prod.description = lista[2]
        stock_prod.instock = int(lista[3])
        stock_prod.id_stock = int(lista[4])
        stock_prod.save()


def method_dispatcher(request, *args, **kwargs):
    '''
        Metodo que redirige al metodo correspondiente segun el metodo de request
    '''
    get_view = kwargs.pop('GET', None)
    post_view = kwargs.pop('POST', None)
    if request.method == 'GET' and get_view is not None:
        return get_view(request, *args, **kwargs)
    elif request.method == 'POST' and post_view is not None:
        return post_view(request, *args, **kwargs)
    raise Http404