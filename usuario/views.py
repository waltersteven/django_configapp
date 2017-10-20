from django.shortcuts import render
import json
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from usuario.forms import RegistroForm
from usuario.serializers import UserSerializer
# Create your views here.
class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('mascota:mascota_listar')

def listadousuarios(request):
    lista = serializers.serialize('json', User.objects.all(), fields=['username', 'first_name', 'last_name'])
    return HttpResponse(lista, content_type='application/json')

class UserAPI(APIView):  #APIView: es una vista de restframework
    serializer = UserSerializer

    def get(self, request, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)  #le indicamos el queryset del cual va a serializar, many=True: porque nos va a devolver muchos registros

        return HttpResponse(json.dumps(response.data), content_type='application/json')  #que de la repsuesta me mande el data