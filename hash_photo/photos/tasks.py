from celery import shared_task
from .models import ItemPhoto
# import pHash
from django.core.files.temp import NamedTemporaryFile


@shared_task
def make_hash(itemPhoto_id):
    recent_photo = ItemPhoto.objects.get(pk=itemPhoto_id)

    # temp = NamedTemporaryFile(delete=False)
    # temp.write(recent_photo.photo.read())
    # hash1 = pHash.imagehash(temp.name)

    hash1 = 'string1'

    recent_photo.phash = str(hash1)
    is_duplicate = ItemPhoto.objects.filter(phash=recent_photo.phash).exists()
    recent_photo.duplicate = is_duplicate
    recent_photo.save(elevation=False)