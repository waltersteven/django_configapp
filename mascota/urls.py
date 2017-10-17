from django.conf.urls import url
from mascota.views import index

urlpatterns = [
    url(r'^$', index),  # ^: es donde inicia la cadena, $: es donde termina
]