# Generated by Django 2.1.1 on 2018-09-03 18:55

import contact.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='profil_picture',
            field=models.ImageField(upload_to=contact.models.content_file_name),
        ),
    ]