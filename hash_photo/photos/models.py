from django.db import models


class ItemPhoto(models.Model):
    photo = models.ImageField(upload_to='photos')
    duplicate = models.BooleanField(default=False)
    phash = models.CharField(max_length=256, blank=True)
