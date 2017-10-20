from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from mascota.forms import MascotaForm
from mascota.models import Mascota, Vacuna
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


# Create your views here.
def listado(request):
    lista = serializers.serialize('json', Mascota.objects.all())
    return HttpResponse(lista, content_type='application/json')

def index(request):
    #return HttpResponse("Index")
    return render(request, 'mascota/index.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)  #se reciben los datos que se mandan en el POST de nuestro formulario
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')  #usando namespaces
    else:  #cuando sea un get
        form = MascotaForm()
    return render(request, 'mascota/mascota_form.html', {'form': form})

def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')  #nos trae todos los ovjetos que están en mascota
    vacuna = Vacuna.objects.all().order_by('id')
    contexto = {'mascotas': mascota, 'vacunas': vacuna}
    return render(request, 'mascota/mascota_list.html', contexto)

def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)  #le mandamos a form una instancia de mascota
    else:
        form = MascotaForm(request.POST, instance=mascota)  #recoge el POST del formulario y su instancia
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')
    return render(request, 'mascota/mascota_form.html', {'form': form})

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:mascota_listar')
    return render(request, 'mascota/mascota_delete.html', {'mascota': mascota})

#Vistas basadas en clases: Vistas genéricas donde se aprovecha POO. Creamos nuestras vistas heredando las de Django.
class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'  #especificamos a qué template enviamos el contexto (object_list)
    paginate_by = 2

    #para enviar mas de un model con ListView
    def get_context_data(self, **kwargs):
        ctx = super(MascotaList, self).get_context_data(**kwargs)
        ctx['vacunas'] = Vacuna.objects.all()
        #And so on for more models
        return ctx

class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')  #con esto hago el redirect

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')

class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascota:mascota_listar')
