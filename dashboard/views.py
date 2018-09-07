from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from event.models import Event


class DashboardView(LoginRequiredMixin, ListView):

    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['event'] = Event.objects.filter(user=self.request.user)

        return context
