from django.contrib import admin
from .models import Catalogue

class CatalogueAdmin(admin.ModelAdmin):
  list_display = ('name', 'file', 'date_created')

  list_display_links = ('name',)
  search_fields = ('name',)
  list_per_page = 25

admin.site.register(Catalogue, CatalogueAdmin)