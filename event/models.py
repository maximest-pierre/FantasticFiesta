from django.db import models

from contact.models import Contact


class Event(models.Model):

    STATUS_CHOICE = (
        ('P', 'Planned'),
        ('O', 'Ongoing'),
        ('C', 'Completed')
    )

    class Meta:
        verbose_name_plural = "Events"

    contact = models.ManyToManyField(Contact, related_name='contact_event')
    status = models.CharField(max_length=1, choices=STATUS_CHOICE)
    note = models.TextField()
    date = models.DateTimeField()
