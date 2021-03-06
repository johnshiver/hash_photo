from django.db import models


class ItemPhoto(models.Model):
    photo = models.ImageField(upload_to='photos')
    duplicate = models.BooleanField(default=False)
    phash = models.CharField(max_length=256, blank=True)

    def save(self, elevation=True, *args, **kwargs):
        super(ItemPhoto, self).save(*args, **kwargs)
        if elevation:
            from photos.tasks import make_hash
            make_hash.delay(self.id)
