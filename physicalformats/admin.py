from django.contrib import admin
from django.db.models import Count
from .models import PhysicalFormat


class PhysicalFormatAdmin(admin.ModelAdmin):
  list_display = ('name', 'books_count', 'date_created')

  list_display_links = ('name',)
  search_fields = ('name',)
  list_per_page = 25

  def get_queryset(self, request):
    return PhysicalFormat.objects.annotate(books_count=Count('book'))

  def books_count(self, obj):
    return obj.books_count
  books_count.short_description = 'عدد الكتب'

admin.site.register(PhysicalFormat, PhysicalFormatAdmin)