from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from books.models import Book
from series.models import Serie
from categories.models import Category
from physicalformats.models import PhysicalFormat

def index(request):
  books = Book.objects.order_by('-date_published', '-date_created').filter(is_published=True)[:3]
  categories_names = Category.objects\
    .order_by('-name')\
    .values_list('id', 'name')

  series_names = Serie.objects\
    .order_by('-name')\
    .values_list('id', 'name')

  physical_formats = PhysicalFormat.objects\
    .order_by('-name')\
    .values_list('id', 'name')
  
  year = datetime.now().year
  dates_published = range(year, year-10, -1)

  context = {
    'books': books,
    'categories': categories_names,
    'series': series_names,
    'dates': dates_published,
    'physical_formats': physical_formats
  }
  return render(request, 'pages/index.html', context)

def about(request):
  return render(request, 'pages/about.html')
