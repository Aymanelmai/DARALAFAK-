import re

from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from datetime import datetime
from physicalformats.models import PhysicalFormat

from .models import Book
from series.models import Serie
from categories.models import Category

def index(request):
  books = Book.objects.order_by('-date_published', '-date_created').filter(is_published=True)
  paginator = Paginator(books, 6)
  page = request.GET.get('page')
  paged_books = paginator.get_page(page)

  context = {
    'books': paged_books
  }
  return render(request, 'books/books.html', context)


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def book(request, book_id):
  book = get_object_or_404(Book, pk=book_id)
  books_ids = [author.id for author in book.authors.all()]
  books_with_same_authors = Book.objects\
    .order_by('-date_published', '-date_created')\
    .filter(authors__in=books_ids)\
    .exclude(pk=book.id)[:3]
  context = {
    'book': book,
    'description': cleanhtml(book.description),
    'books_with_same_authors': books_with_same_authors
  }
  return render(request, 'books/single_book.html', context)

def search(request):
  queryset_list = Book.objects.order_by('-date_created')
  
  for param in request.GET:
    if request.GET[param]:
      key = param
      if 'id' not in param :
        key += '__icontains'
      kwargs = {key: request.GET[param].strip()}
      queryset_list = queryset_list.filter(**kwargs)

  categories_names = Category.objects\
    .order_by('-name')\
    .values_list('id', 'name')
  categories_names = map( lambda x: [ str(x[0]), str(x[1]) ]
    ,categories_names)

  series_names = Serie.objects\
    .order_by('-name')\
    .values_list('id', 'name')
  series_names = map( lambda x: [ str(x[0]), str(x[1]) ]
    ,series_names)

  physical_formats = PhysicalFormat.objects\
    .order_by('-name')\
    .values_list('id', 'name')
  physical_formats = map( lambda x: [ str(x[0]), str(x[1]) ]
    ,physical_formats)

  year = datetime.now().year
  dates_published = range(year, year-10, -1)
  dates_published = map( lambda x: str(x) 
    ,dates_published)
  
  context = {
    'books': queryset_list.distinct(),
    'categories': categories_names,
    'series': series_names,
    'dates': dates_published,
    'physical_formats': physical_formats,
    'values': request.GET
  }

  return render(request, 'books/search.html', context)
