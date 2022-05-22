from django.contrib import admin
from .models import *

# Register your models here.

class Upcoming_EventAdmin(admin.ModelAdmin):
	list_display= ['title', 'slug','program_date', 'pub_date' ]
	prepopulated_fields= {'slug': ('title',)}

class GalleryImageInline(admin.StackedInline):
	model=GalleryImage

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
	list_display=['title']
	inlines= [GalleryImageInline]

admin.site.register(Upcoming_Event, Upcoming_EventAdmin)
admin.site.register(GalleryImage)



