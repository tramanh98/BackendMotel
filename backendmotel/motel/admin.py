from django.contrib import admin

# Register your models here.
from .models import Motel, ImageMotel

admin.site.register(ImageMotel)

@admin.register(Motel)
class Motel(admin.ModelAdmin):
    list_display = ('title', 'content', 'typeMotel', 'district', 'address', 'price', 'created_at')
    raw_id_fields = ('user',)
    list_filter = ('typeMotel', 'address', 'ward', 'district')
    search_fields = ('title', 'user__username', 'user__email')

