from django.conf.urls import url
from mascota.views import listado, index, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index, name='index'),  # ^: es donde inicia la cadena, $: es donde termina la cadena del url
    url(r'^nuevo$', login_required(MascotaCreate.as_view()), name='mascota_crear'),  #cuando consulta /nuevo/ consulta a mascota_view
    url(r'^listar', login_required(MascotaList.as_view()), name= 'mascota_listar'),  #le quito el dolar porque despues del listar se añadira el parametro de paginación
    url(r'^editar/(?P<pk>\d+)/$', login_required(MascotaUpdate.as_view()), name='mascota_editar'),  #pk equivale a id_mascota en clase-based views
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
    url(r'^listado/', listado, name="listado"),
]