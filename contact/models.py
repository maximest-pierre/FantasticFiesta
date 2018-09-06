import random

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


def content_file_name(instance, filename):
    return '/'.join(['content', str(random.getrandbits(128))])


class Contact(models.Model):

    class Meta:
        verbose_name_plural = "Contacts"

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    profil_picture = models.ImageField(upload_to=content_file_name)

    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    def __str__(self):
        return "%s, %s created by %s" % (
            self.last_name, self.first_name, self.added_by
        )
