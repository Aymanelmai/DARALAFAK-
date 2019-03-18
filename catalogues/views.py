from django.shortcuts import render
from .models import Catalogue

def index(request):
  catalogues = Catalogue.objects.all()
  context = {
    'catalogues': catalogues
  }
  return render(request, 'catalogues/catalogues.html', context)