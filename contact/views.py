from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from contact.models import Contact


class ListContact(ListView, LoginRequiredMixin):
    model = Contact

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['contacts'] = Contact.objects.filter(added_by=self.request.user)

        return context


class CreateContact(CreateView, LoginRequiredMixin):
    model = Contact
    template_name = 'contact/create_contact.html'

    fields = ['first_name', 'last_name', 'email', 'profil_picture']

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        contact = Contact()
        if form.is_valid():
            contact.email = form.cleaned_data['email']
            contact.first_name = form.cleaned_data['first_name']
            contact.last_name = form.cleaned_data['last_name']
            contact.profil_picture = form.cleaned_data['profil_picture']
            contact.added_by = self.request.user
            contact.save()
            return HttpResponseRedirect('/contact/')
        else:
            return render(request, self.template_name, {'form': form})


class DetailContact(DetailView, LoginRequiredMixin):
    model = Contact
    template_name = 'contact/detail_contact.html'


class UpdateContact(UpdateView, LoginRequiredMixin):
    model = Contact
    template_name = 'contact/create_contact.html'

    fields = ['first_name', 'last_name', 'email', 'profil_picture']
    success_url = '/contact/'


class DeleteContact(DeleteView, LoginRequiredMixin):
    model = Contact
    template_name = 'contact/delete_contact.html'
    success_url = '/contact/'
