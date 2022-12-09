from django.contrib import admin

# Register your models here.
from .models import *

class ResourceAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'author', 'link')
	list_display_links = ('id', 'name')
	search_fields = ['author']

admin.site.register(Resource, ResourceAdmin)
admin.site.register(Article)