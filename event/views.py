from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from event.forms import CreateEventForm
from event.models import Event


class CreateEvent(CreateView, LoginRequiredMixin):
    model = Event
    template_name = 'event/create_event.html'
    form_class = CreateEventForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        event = Event()
        if form.is_valid():
            event.contact = form.cleaned_data['contact']
            event.date = form.cleaned_data['date']
            event.note = form.cleaned_data['note']
            event.status = form.cleaned_data['status']
            event.user = self.request.user
            event.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, self.template_name, {'form': form})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class UpdateEvent(UpdateView, LoginRequiredMixin):
    model = Event
    template_name = 'event/update_event.html'
    form_class = CreateEventForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class DeleteEvent(DeleteView, LoginRequiredMixin):
    model = Event
    template_name = 'event/delete_event.html'
    success_url = '/'
