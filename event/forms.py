from django.forms.models import ModelForm
from event.models import Event


class CreateEventForm(ModelForm):

    class Meta:
        fields = ['contact', 'status', 'note', 'date']
        model = Event
        labels = {
            'date': 'Date and Time'
        }
        help_texts = {
            'date': 'Date and Time in format DD/MM/YYYY hh:mm',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['contact'].queryset = self.fields['contact'].queryset.filter(
            added_by=user)
