from django.db import models


class ItemPhoto(models.Model):
    photo = models.ImageField(upload_to='photos')
    name = models.CharField(max_length=100)
