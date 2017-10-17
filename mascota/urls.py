from django.conf.urls import url
from mascota.views import index, mascota_view, mascota_list

urlpatterns = [
    url(r'^$', index, name='index'),  # ^: es donde inicia la cadena, $: es donde termina
    url(r'^nuevo$', mascota_view, name='mascota_crear'),  #cuando consulta /nuevo/ consulta a mascota_view
    url(r'^listar$', mascota_list, name= 'mascota_listar'),
]