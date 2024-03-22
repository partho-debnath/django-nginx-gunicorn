from django.contrib import admin

from app.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
