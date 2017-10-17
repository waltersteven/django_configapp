from django.shortcuts import render, redirect
from django.http import HttpResponse
from mascota.forms import MascotaForm

# Create your views here.
def index(request):
    #return HttpResponse("Index")
    return render(request, 'mascota/index.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)  #se reciben los datos que se mandan en el POST de nuestro formulario
        if form.is_valid():
            form.save()
        return redirect('mascota:index')  #usando namespaces
    else:  #cuando sea un get
        form = MascotaForm()
    return render(request, 'mascota/mascota_form.html', {'form': form})