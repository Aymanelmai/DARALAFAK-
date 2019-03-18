from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Author
from books.models import Book

def index(request):
  authors = Author.objects.order_by('name')
  paginator = Paginator(authors, 6)
  page = request.GET.get('page')
  paged_authors = paginator.get_page(page)
  context = {
    'authors': paged_authors
  }
  return render(request, 'authors/authors.html', context)

def author(request, author_id):
  author = get_object_or_404(Author, pk=author_id)
  books_with_same_author = Book.objects\
    .order_by('-date_created')\
    .filter(authors__id=author.id)

  context = {
    'author': author,
    'books': books_with_same_author
  }
  return render(request, 'authors/author.html', context)