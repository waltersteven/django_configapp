from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from adopcion.models import Persona, Solicitud
from adopcion.forms import PersonaForm, SolicitudForm
from django.core.urlresolvers import reverse_lazy
# Create your views here.
def index_adopcion(request):
    return HttpResponse("Esta es la página principal del app adopción")

class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopcion/solicitud_list.html'

class SolicitudCreate(CreateView):
    model = Solicitud
    template_name = 'adopcion/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm  #es el 2do formulario, cuando llenemos el primero, por detrás también se llenará este.
    success_url = reverse_lazy('adopcion:solicitud_listar')

    #agregamos el form1 y form2 a nuestro contexto
    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    #redefinimos el método POST
    def post(self, request, *args, **kwargs):  #recibe argumentos y keywords
        self.object = self.get_object
        form = self.form_class(request.POST)  #recogemos los valores de form y form2
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)  #commit=False para que no guarde los valores hasta que se guarde el 2do formulario
            solicitud.persona = form2.save()  #Creamos la relación (los valores de persona serán igual a los valores ingresados en form2)
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class SolicitudUpdate(UpdateView):
    model = Solicitud
    second_model = Persona
    template_name = 'adopcion/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('adopcion:solicitud_listar')

    def get_context_data(self, **kwargs):
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)  #obteniendo los keywords
        solicitud = self.model.objects.get(id=pk)  #obtenemos el objeto solicitud
        persona = self.second_model.objects.get(id=solicitud.persona_id)  #obtenemos el objeto persona

        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']  #obtenemos el id
        solicitud = self.model.objects.get(id=id_solicitud)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        form = self.form_class(request.POST, instance=solicitud)  #instance es para que no cree objeto y lo actualice
        form2 = self.second_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name = 'adopcion/solicitud_delete.html'
    success_url = reverse_lazy('adopcion:solicitud_listar')


