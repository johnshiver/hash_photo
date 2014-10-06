from celery import task
from .models import ItemPhoto


@task
def add(x, y):
    return x + y


@task
def dummy_hash(itemPhoto_id):
    recent_photo = ItemPhoto.objects.get(pk=itemPhoto_id)
    recent_photo.phash = 'thisIsABigHashNumber'
    is_duplicate = ItemPhoto.objects.filter(phash=recent_photo.phash).exists()
    recent_photo.duplicate = is_duplicate
    recent_photo.save(elevation=False)
