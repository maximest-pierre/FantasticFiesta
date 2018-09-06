# Generated by Django 2.1.1 on 2018-09-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20180906_0305'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='contact',
        ),
        migrations.AddField(
            model_name='event',
            name='contact',
            field=models.ManyToManyField(related_name='contact_event', to='contact.Contact'),
        ),
    ]