from django.contrib import admin
from .models import ZonesProtgesDuSngal, ImageFile


# Register your models here.

admin.site.register(ZonesProtgesDuSngal)


@admin.register(ImageFile)
class ImageFileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'Country_name')


