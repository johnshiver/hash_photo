from django.contrib import admin
from photos.models import ItemPhoto


class ItemPhotoAdmin(admin.ModelAdmin):

    def file_name(self, ItemPhoto):
        """
        returns name of image without the /photos
        """
        return ItemPhoto.photo.name[7:]
    file_name.short_description = 'fileName (ImageField)'

    def duplicate_repr(self, ItemPhoto):
        """
        represents duplicate as X or []
        """
        representation = None
        if ItemPhoto.duplicate:
            representation = 'X'
        else:
            representation = '[]'
        return representation
    duplicate_repr.short_description = 'Duplicate? (bool)'

    def phash_repr(self, ItemPhoto):
        """
        represents Hash with its first 14 characters followed by ....
        """
        representation = None
        if len(ItemPhoto.phash) > 14:
            representation = ItemPhoto.phash[:14] + '....'
        else:
            representation = ItemPhoto.phash
        return representation
    phash_repr.short_description = 'Hash (Char)'

    def id_repr(self, ItemPhoto):
        return ItemPhoto.id
    id_repr.short_description = 'ID (auto generated)'

    fields = ('photo',
              'duplicate',
              'phash')

    list_display = ('id_repr',
                    'file_name',
                    'duplicate_repr',
                    'phash_repr')

    ordering = ['id']
admin.site.register(ItemPhoto, ItemPhotoAdmin)
