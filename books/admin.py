from django.contrib import admin
from .models import Book
from authors.models import Author

class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'authors_names'
    , 'category', 'pages', 'price'
    , 'is_published', 'is_available'
    , 'date_created')
  
  list_display_links = ('title',)
  list_filter = ('authors', 'category')
  list_editable = ('is_published',)
  search_fields = ('title', 'description',)
  list_per_page = 25
  autocomplete_fields = ['authors', 'publisher', 'category', 'serie']

admin.site.register(Book, BookAdmin)
