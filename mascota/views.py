from django.shortcuts import render, redirect
from django.http import HttpResponse
from mascota.forms import MascotaForm
from mascota.models import Mascota, Vacuna
# Create your views here.
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