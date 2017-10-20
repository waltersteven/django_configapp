from django.conf.urls import url
from usuario.views import RegistroUsuario, listadousuarios, UserAPI

urlpatterns = [
    url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
    url(r'^listadousuarios/', listadousuarios, name="listadousuarios"),  #sin usar djangorestframework
    url(r'^api', UserAPI.as_view(), name="api"),  #usando djangorestframework
]