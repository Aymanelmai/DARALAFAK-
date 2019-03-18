from django.contrib import admin
from django.db.models import Count
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
  list_display = ('name', 'books_count', 'date_created')

  list_display_links = ('name',)
  search_fields = ('name',)
  list_per_page = 25

admin.site.register(Author, AuthorAdmin)